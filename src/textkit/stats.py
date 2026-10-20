"""Text statistics."""


def word_count(text: str) -> int:
    """Number of whitespace-separated words."""
    return len(text.split())
