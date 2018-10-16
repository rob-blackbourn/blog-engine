def group_by(iterable, key_selector, projection=None):
    """
    Returns an iterator which groups the iterable with a key provided by the
    supplied function. The source iterable does not need to be sorted.

    :param iterable: The items over which to iterate.
    :param key_selector: A function which selects the key to group on.
    :return: A tuple of the key and the list of items matching the key.
    """
    groups = {}
    for item in iterable:
        key = key_selector(item)
        value = projection(item) if projection else item
        if key in groups:
            groups[key].append(value)
        else:
            groups[key] = [value]
    return groups


def first_or_default(iterable, predicate=None, default=None):
    """First the first value matching a perdicate otherwise a default value.

    :param iterable: The items over which to iterate.
    :param predicate: A predicate to apply to each item.
    :param default: The value to return if no item matches.
    :return: The first value matching a predicate otherwise the default value.
    """
    for item in iterable:
        if not predicate or predicate(item):
            return item
    return default
