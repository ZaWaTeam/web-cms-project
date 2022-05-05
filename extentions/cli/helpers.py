def find_filter(key, value, dict):
    find = filter(lambda c: c[key] == value, dict)

    return bool(len(list(find)))
