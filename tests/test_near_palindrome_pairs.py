import pytest
from src.near_palindrome_pairs import find_near_palindrome_pairs

def test_basic_near_palindrome_pairs():
    """Test finding basic near palindrome pairs"""
    input_strings = ['racecar', 'hello', 'level', 'radar']
    result = find_near_palindrome_pairs(input_strings)
    assert len(result) > 0, "Should find near palindrome pairs"
    assert all(len(pair) == 2 for pair in result), "Each result should be a pair"

def test_empty_list():
    """Test with an empty list"""
    result = find_near_palindrome_pairs([])
    assert result == [], "Should return an empty list for empty input"

def test_near_palindrome_detection():
    """Test specific near palindrome scenarios"""
    input_strings = ['racecap', 'abcde', 'xamax', 'hello']
    result = find_near_palindrome_pairs(input_strings)
    
    # Verify that pairs with near palindromes are detected
    expected_pairs = [
        ['racecap', 'xamax'],  # These can become palindromes by changing one character
        ['racecap', 'abcde'],
        ['xamax', 'abcde']
    ]
    
    # Check that at least some expected pairs are found
    found_pairs = any(
        any(set(expected_pair) == set(pair) for expected_pair in expected_pairs) 
        for pair in result
    )
    assert found_pairs, "Should detect near palindrome pairs"

def test_invalid_input_types():
    """Test error handling for invalid input types"""
    with pytest.raises(TypeError):
        find_near_palindrome_pairs("not a list")
    
    with pytest.raises(TypeError):
        find_near_palindrome_pairs(None)

def test_list_with_non_string_elements():
    """Test error handling for lists with non-string elements"""
    with pytest.raises(ValueError):
        find_near_palindrome_pairs([1, 'hello', 3])

def test_no_near_palindromes():
    """Test scenario with no near palindromes"""
    input_strings = ['hello', 'world', 'python']
    result = find_near_palindrome_pairs(input_strings)
    assert result == [], "Should return an empty list when no near palindromes exist"