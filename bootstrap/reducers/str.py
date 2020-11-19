def reduce_strings(description, locale=None):
    if locale is None:
        locales = {}

        if isinstance(description.locales, dict):
            for key, value in description.locales.items():
                locales[key] = reduce_strings(description, key)

        return locales
    
    locales = []
    
    if isinstance(description.locales, dict):
        if locale in description.locales.keys():
            locales.append({
                "key": description.id,
                "value": description.locales[locale]
            })

    if isinstance(description.value, list):
        for item in description.value:
            locales = locales + list(filter(None, reduce_strings(item, locale)))

    return locales