

def count_in_list(words: list, find: str) -> int:
    """Return how many times find appears in words."""
    result = 0
    for content in words:
        if content == find:
            result = result + 1

    return (result)
