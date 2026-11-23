

def ft_filter(function, iterable):
    """Return an iterator yielding those items of iterable for which
    function(item) is true.  If function is None, return the items that
    are true."""

    for content in iterable:
        if function(content):
            yield content
