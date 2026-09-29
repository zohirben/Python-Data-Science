def ft_filter(function, iterable):
    """Return an iterator."""
    for item in iterable:
        if function is None:
            if item:
                yield item
        elif function(item):
            yield item


ft_filter.__doc__ = filter.__doc__
