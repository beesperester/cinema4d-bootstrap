"""
This module provides generic Description classes and sugared classes
"""

import hashlib


class IdError(Exception):
    """
    ID Error Exception class
    """


class Description(object):
    """
    This class models a generic description
    """

    def __init__(
        self,
        config: dict
    ) -> None:
        """
        This method initializes a new instance of the Description class
        """
        default_config = {
            "id": None,
            "key": None,
            "value": None,
            "locales": None
        }

        self.config = {**default_config, **config}

    def __getattr__(
        self,
        name: str
    ) -> any:
        """
        This method implements __getattr__ for looking up
        attributes from config dictionary
        """
        if name in self.config.keys():
            return self.config[name]

        raise AttributeError(
            "type object 'Description' has no attribute '{}'".format(name)
        )

    def GetId(self) -> int:
        """
        This method implements the hashing of the id attribute
        as an integer
        """
        if not self.id:
            raise IdError("No id has been assigned")

        return int(
            hashlib.sha1(self.id.encode('utf-8')).hexdigest(), 16
        ) % (10 ** 8)


class Assignment(Description):
    """
    This class provides sugar for an Assignment type Description
    """

    def __init__(
        self,
        key: str = None,
        value: any = None,
        config: dict = None
    ) -> None:
        """
        This method initializes a new instance of the Assignment class
        """
        if config is None:
            config = {}

        default_config = {
            **config,
            "key": key,
            "value": value
        }

        super(Assignment, self).__init__(default_config)


class Group(Description):
    """
    This class provides sugar for a Group type Description
    """

    def __init__(
        self,
        description_id: str,
        config: dict = None
    ) -> None:
        """
        This method initializes a new instance of the Group class
        """
        if config is None:
            config = {}

        default_config = {
            **config,
            "id": description_id,
            "key": "GROUP"
        }

        super(Group, self).__init__(default_config)


class Container(Description):
    """
    This class provides sugar for a Container type Description
    """

    def __init__(
        self,
        description_id: str,
        config: dict = None
    ) -> None:
        """
        This method initializes a new instance of the Container class
        """
        if config is None:
            config = {}

        default_config = {
            **config,
            "id": description_id,
            "key": "CONTAINER"
        }

        super(Container, self).__init__(default_config)
