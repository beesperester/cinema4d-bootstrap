def reduce_resource(description):
    data = {
        "id": description.id,
        "key": description.key
    }

    if isinstance(description.value, list):
        data["value"] = [reduce_resource(x) for x in description.value]
    else:
        data["value"] = description.value

    return data