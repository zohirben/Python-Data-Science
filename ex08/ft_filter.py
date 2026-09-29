def ft_filter(function, iterable):
    """Return an iterator yielding those items of iterable for which function(item) is true."""
    for item in iterable:
        if function is None:
            if item:
                yield item
        elif function(item):
            yield item