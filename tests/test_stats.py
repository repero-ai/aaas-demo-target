from textkit.stats import word_count


def test_word_count():
    assert word_count("a b  c\nd") == 4
    assert word_count("") == 0
