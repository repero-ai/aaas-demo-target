"""Case conversion helpers."""

import re


def slugify(text: str) -> str:
    """Lowercase, keep ASCII letters/digits, join words with '-'."""
    words = re.findall(r"[a-z0-9]+", text.lower())
    return "-".join(words)


def to_snake_case(text: str) -> str:
    """Convert CamelCase or spaced text to snake_case."""
    text = re.sub(r"([a-z0-9])([A-Z])", r"\1_\2", text)
    return "_".join(re.findall(r"[a-z0-9]+", text.lower()))


def to_kebab_case(text: str) -> str:
    """Convert CamelCase or spaced text to kebab-case."""
    text = re.sub(r"([a-z0-9])([A-Z])", r"\1-\2", text)
    return "-".join(re.findall(r"[a-z0-9]+", text.lower()))
