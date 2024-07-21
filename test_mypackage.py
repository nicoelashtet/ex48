import pytest
from ex48 import WORD_TYPES, convert_number, scan

def test_word_types():
    assert WORD_TYPES["north"] == "direction"
    assert WORD_TYPES["south"] == "direction"
    assert WORD_TYPES["east"] == "direction"
    assert WORD_TYPES["west"] == "direction"
    assert WORD_TYPES["go"] == "verb"
    assert WORD_TYPES["kill"] == "verb"
    assert WORD_TYPES["eat"] == "verb"
    assert WORD_TYPES["the"] == "stop"
    assert WORD_TYPES["in"] == "stop"
    assert WORD_TYPES["of"] == "stop"
    assert WORD_TYPES["bear"] == "noun"
    assert WORD_TYPES["princess"] == "noun"

def test_convert_number():
    assert convert_number("1234") == 1234
    assert convert_number("3") == 3
    assert convert_number("91234") == 91234
    assert convert_number("abc") is None

def test_scan():
    assert scan("north") == [("direction", "north")]
    assert scan("north south east") == [("direction", "north"), ("direction", "south"), ("direction", "east")]
    assert scan("go kill eat") == [("verb", "go"), ("verb", "kill"), ("verb", "eat")]
    assert scan("the in of") == [("stop", "the"), ("stop", "in"), ("stop", "of")]
    assert scan("bear princess") == [("noun", "bear"), ("noun", "princess")]
    assert scan("1234") == [("number", 1234)]
    assert scan("bear eat 1234") == [("noun", "bear"), ("verb", "eat"), ("number", 1234)]
    assert scan("ASDFG QWERTY") == [("error", "ASDFG"), ("error", "QWERTY")]
