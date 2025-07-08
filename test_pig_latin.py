import pytest
from pig_latin import pl_word, pl_sentence


@pytest.mark.parametrize("word, expected", [
    ('apple', 'appleway'),
    ('elephant', 'elephantway'),
    ('orange', 'orangeway'),
    ('umbrella', 'umbrellaway'),
    ('ice', 'iceway'),
    ('a', 'away'),
    ('i', 'iway'),
    ('at', 'atway'),
    ('it', 'itway'),
])
def test_pl_word_vowels(word, expected):
    """Test words that start with vowels."""
    assert pl_word(word) == expected


@pytest.mark.parametrize("word, expected", [
    ('computer', 'omputercay'),
    ('banana', 'ananabay'),
    ('python', 'ythonpay'),
    ('hello', 'ellohay'),
    ('world', 'orldway'),
    ('b', 'bay'),
    ('x', 'xay'),
    ('by', 'ybay'),
    ('to', 'otay'),
])
def test_pl_word_consonants(word, expected):
    """Test words that start with consonants."""
    assert pl_word(word) == expected


def test_pl_word_empty_string():
    """Test that empty string raises an IndexError."""
    with pytest.raises(IndexError):
        pl_word('')


@pytest.mark.parametrize("sentence, expected", [
    ('hello world', 'ellohay orldway'),
    ('apple banana', 'appleway ananabay'),
    ('this is a test', 'isthay isway away esttay'),
    ('computer', 'omputercay'),
    ('apple', 'appleway'),
    ('', ''),
    ('hello  world', 'ellohay orldway'),
])
def test_pl_sentence(sentence, expected):
    """Test sentence translation with various inputs."""
    assert pl_sentence(sentence) == expected