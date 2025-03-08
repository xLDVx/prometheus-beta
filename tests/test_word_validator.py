import pytest
from src.word_validator import Queue, is_word_valid

# Queue tests
def test_queue_basic_operations():
    q = Queue()
    assert q.is_empty() == True
    assert q.size() == 0
    
    q.enqueue(1)
    assert q.is_empty() == False
    assert q.size() == 1
    assert q.peek() == 1
    
    item = q.dequeue()
    assert item == 1
    assert q.is_empty() == True
    assert q.size() == 0

def test_queue_multiple_items():
    q = Queue()
    q.enqueue(1)
    q.enqueue(2)
    q.enqueue(3)
    
    assert q.size() == 3
    assert q.peek() == 1
    
    assert q.dequeue() == 1
    assert q.dequeue() == 2
    assert q.dequeue() == 3
    assert q.is_empty() == True

def test_queue_error_handling():
    q = Queue()
    
    with pytest.raises(IndexError, match="Cannot peek an empty queue"):
        q.peek()
    
    with pytest.raises(IndexError, match="Cannot dequeue from an empty queue"):
        q.dequeue()

# is_word_valid tests
def test_is_word_valid_basic():
    # Test basic scenarios
    assert is_word_valid("hello", {"min_length": 3, "max_length": 5}) == True
    assert is_word_valid("a", {"min_length": 3, "max_length": 5}) == False
    assert is_word_valid("toolongword", {"min_length": 3, "max_length": 5}) == False

def test_is_word_valid_allowed_chars():
    # Test allowed characters
    assert is_word_valid("abc", {"allowed_chars": "abc"}) == True
    assert is_word_valid("def", {"allowed_chars": "abc"}) == False

def test_is_word_valid_starts_with():
    # Test starts_with rule
    assert is_word_valid("hello", {"starts_with": ["he", "hi"]}) == True
    assert is_word_valid("world", {"starts_with": ["he", "hi"]}) == False

def test_is_word_valid_ends_with():
    # Test ends_with rule
    assert is_word_valid("coding", {"ends_with": ["ing", "ed"]}) == True
    assert is_word_valid("code", {"ends_with": ["ing", "ed"]}) == False

def test_is_word_valid_combined_rules():
    # Test multiple rules together
    rules = {
        "min_length": 4,
        "max_length": 6,
        "allowed_chars": "abcdef",
        "starts_with": ["a", "b"],
        "ends_with": ["ed"]
    }
    assert is_word_valid("abbed", rules) == True
    assert is_word_valid("abc", rules) == False  # too short
    assert is_word_valid("abcdefg", rules) == False  # too long
    assert is_word_valid("xyz", rules) == False  # disallowed chars
    assert is_word_valid("caded", rules) == False  # doesn't start with a/b

def test_is_word_valid_input_validation():
    # Test input type validation
    assert is_word_valid(123, {}) == False
    assert is_word_valid("hello", None) == False