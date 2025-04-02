import os
import pytest
from src.word_list_processor import process_word_list

def test_process_word_list_basic():
    # Create a test input file
    with open('tests/test_input.txt', 'w') as f:
        f.write("apple\nbanana\ncherry\napple\ndate\nbanana")
    
    # Process the file
    result = process_word_list('tests/test_input.txt')
    
    # Expected sorted unique words
    expected = ['apple', 'banana', 'cherry', 'date']
    
    assert result == expected, f"Expected {expected}, but got {result}"
    
    # Clean up the test file
    os.remove('tests/test_input.txt')

def test_process_word_list_empty_file():
    # Create an empty test file
    with open('tests/empty_input.txt', 'w') as f:
        pass
    
    # Process the empty file
    result = process_word_list('tests/empty_input.txt')
    
    # Expected empty list
    assert result == [], "Expected an empty list for an empty input file"
    
    # Clean up the test file
    os.remove('tests/empty_input.txt')

def test_process_word_list_non_existent_file():
    # Attempt to process a non-existent file should raise FileNotFoundError
    with pytest.raises(FileNotFoundError):
        process_word_list('tests/non_existent_file.txt')

def test_process_word_list_case_insensitive():
    # Create a test input file with mixed case
    with open('tests/case_input.txt', 'w') as f:
        f.write("Apple\nBANANA\ncherry\napple\nDATE\nbanana")
    
    # Process the file
    result = process_word_list('tests/case_input.txt')
    
    # Expected sorted unique words (lowercase)
    expected = ['apple', 'banana', 'cherry', 'date']
    
    assert result == expected, f"Expected {expected}, but got {result}"
    
    # Clean up the test file
    os.remove('tests/case_input.txt')