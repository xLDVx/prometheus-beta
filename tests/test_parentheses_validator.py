import pytest
from src.parentheses_validator import is_balanced_parentheses

def test_simple_balanced():
    assert is_balanced_parentheses("()") == True

def test_nested_balanced():
    assert is_balanced_parentheses("((()))") == True

def test_multiple_sets_balanced():
    assert is_balanced_parentheses("(()())") == True

def test_unbalanced_missing_closing():
    assert is_balanced_parentheses("((()") == False

def test_unbalanced_missing_opening():
    assert is_balanced_parentheses("())") == False

def test_invalid_order():
    assert is_balanced_parentheses(")(") == False

def test_empty_string():
    assert is_balanced_parentheses("") == True

def test_mixed_parentheses_balanced():
    assert is_balanced_parentheses("([{}])") == True

def test_mixed_parentheses_unbalanced():
    assert is_balanced_parentheses("([)]") == False

def test_string_with_other_characters():
    assert is_balanced_parentheses("a(b)c(d)e") == True
    assert is_balanced_parentheses("a(b(c)d") == False

def test_only_opening_parentheses():
    assert is_balanced_parentheses("(((") == False

def test_only_closing_parentheses():
    assert is_balanced_parentheses(")))") == False