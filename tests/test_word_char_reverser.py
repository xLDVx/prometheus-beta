import pytest
from src.word_char_reverser import reverse_words_and_chars

def test_basic_reversal():
    """Test basic word and character reversal."""
    assert reverse_words_and_chars("Hello World") == "dlroW olleH"

def test_multiple_words():
    """Test reversal of multiple words."""
    assert reverse_words_and_chars("Python is awesome") == "emosewa si nohtyP"

def test_empty_string():
    """Test handling of empty string."""
    assert reverse_words_and_chars("") == ""

def test_single_word():
    """Test reversal of a single word."""
    assert reverse_words_and_chars("Python") == "nohtyP"

def test_string_with_spaces():
    """Test handling of string with extra spaces."""
    assert reverse_words_and_chars("  Hello   World  ") == "dlroW olleH"

def test_string_with_punctuation():
    """Test handling of string with punctuation."""
    assert reverse_words_and_chars("Hello, World!") == "!dlroW ,olleH"