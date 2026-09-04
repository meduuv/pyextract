def get_path(data, path, default=None):
    """Read a dotted path from nested dictionaries and sequences."""
    if not path:
        return data
    current = data
    for part in path.split("."):
        try:
            if isinstance(current, dict):
                current = current[part]
            elif isinstance(current, (list, tuple)):
                current = current[int(part)]
            else:
                return default
        except (KeyError, IndexError, TypeError, ValueError):
            return default
    return current


def first_present(data, keys, default=None):
    """Return the first value whose key exists in a mapping."""
    for key in keys:
        if key in data:
            return data[key]
    return default
