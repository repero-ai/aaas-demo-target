from textkit.case import slugify, to_snake_case


def test_slugify():
    assert slugify("Hello, World!") == "hello-world"


def test_to_snake_case():
    assert to_snake_case("HelloWorld") == "hello_world"
    assert to_snake_case("hello world") == "hello_world"
