import os
import pytest
from src.sum_pairs_diff_nine import find_sum_of_pairs_with_diff_nine

def test_basic_pairs():
    # Create a test file with basic pairs
    with open('tests/test_numbers.txt', 'w') as f:
        f.write("1\n10\n5\n14\n20\n11\n")
    
    # Pairs with difference of 9: (1,10), (5,14)
    # Total sum: (1+10) + (5+14) = 30
    assert find_sum_of_pairs_with_diff_nine('tests/test_numbers.txt') == 30

def test_no_pairs():
    # Create a file with no pairs having difference of 9
    with open('tests/test_numbers.txt', 'w') as f:
        f.write("1\n2\n3\n4\n5\n")
    
    assert find_sum_of_pairs_with_diff_nine('tests/test_numbers.txt') == 0

def test_duplicate_pairs():
    # Create a file with multiple instances of pairs
    with open('tests/test_numbers.txt', 'w') as f:
        f.write("1\n10\n1\n10\n5\n14\n")
    
    # Pairs with difference of 9: (1,10), (1,10), (5,14)
    # Total sum: (1+10) + (1+10) + (5+14) = 60
    assert find_sum_of_pairs_with_diff_nine('tests/test_numbers.txt') == 60

def test_empty_file():
    # Create an empty file
    with open('tests/test_numbers.txt', 'w') as f:
        pass
    
    assert find_sum_of_pairs_with_diff_nine('tests/test_numbers.txt') == 0

def test_file_not_found():
    # Test file not found scenario
    with pytest.raises(FileNotFoundError):
        find_sum_of_pairs_with_diff_nine('tests/nonexistent_file.txt')

def test_invalid_content():
    # Create a file with non-numeric content
    with open('tests/test_numbers.txt', 'w') as f:
        f.write("1\n2\nabc\n4\n")
    
    with pytest.raises(ValueError):
        find_sum_of_pairs_with_diff_nine('tests/test_numbers.txt')

def test_negative_numbers():
    # Create a file with negative numbers
    with open('tests/test_numbers.txt', 'w') as f:
        f.write("-1\n8\n-10\n-1\n")
    
    # Pairs with difference of 9: (-10,-1), (-1,8)
    # Total sum: (-10-1) + (-1+8) = -12
    assert find_sum_of_pairs_with_diff_nine('tests/test_numbers.txt') == -3

# Clean up after tests
def teardown_module(module):
    # Remove test file if it exists
    if os.path.exists('tests/test_numbers.txt'):
        os.remove('tests/test_numbers.txt')