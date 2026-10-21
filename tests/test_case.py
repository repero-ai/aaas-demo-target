from textkit.case import slugify, to_kebab_case, to_snake_case


def test_slugify():
    assert slugify("Hello, World!") == "hello-world"


def test_to_snake_case():
    assert to_snake_case("HelloWorld") == "hello_world"
    assert to_snake_case("hello world") == "hello_world"


def test_to_kebab_case():
    assert to_kebab_case("HelloWorld") == "hello-world"
    assert to_kebab_case("hello world") == "hello-world"
