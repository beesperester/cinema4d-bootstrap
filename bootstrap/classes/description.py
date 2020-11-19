import hashlib

class IdError(Exception):
    """ID Error"""

class Description(object):

    def __init__(self, config):
        default_config = {
            "id": None,
            "key": None,
            "value": None,
            "locales": None
        }

        self.config = {**default_config, **config}

    def __getattr__(self, name):
        if name in self.config.keys():
            return self.config[name]

        raise AttributeError("type object 'Description' has no attribute '{}'".format(name))

    def GetId(self):
        if not self.id:
            raise IdError("No id has been assigned")

        return int(hashlib.sha1(self.id.encode('utf-8')).hexdigest(), 16) % (10 ** 8)

class Assignment(Description):

    def __init__(self, key = None, value = None, config = None):
        if config is None:
            config = {}

        default_config = {
            **config,
            "key": key,
            "value": value
        }

        super(Assignment, self).__init__(default_config)

class Group(Description):

    def __init__(self, description_id, config):
        default_config = {
            **config,
            "id": description_id,
            "key": "GROUP"
        }

        super(Group, self).__init__(default_config)

class Container(Description):
    
    def __init__(self, description_id, config):
        default_config = {
            **config,
            "id": description_id,
            "key": "CONTAINER"
        }

        super(Container, self).__init__(default_config)