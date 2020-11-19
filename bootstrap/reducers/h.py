from bootstrap.classes.description import IdError

def reduce_header(description):
    data = []

    try:
        data.append({
            "key": description.id,
            "value": description.GetId()
        })
    except IdError:
        pass

    if isinstance(description.value, list):
        for item in description.value:
            data = data + list(filter(None, reduce_header(item)))

    return data