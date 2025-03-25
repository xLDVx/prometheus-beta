import os
import pytest
from src.file_reader import read_file_lines

def test_read_file_lines_successful():
    # Create a temporary test file
    test_file_path = 'tests/test_file.txt'
    with open(test_file_path, 'w') as f:
        f.write("Hello\nWorld\nPython")
    
    # Read the file
    lines = read_file_lines(test_file_path)
    
    # Check the content
    assert lines == ['Hello', 'World', 'Python']
    
    # Clean up
    os.remove(test_file_path)

def test_read_file_lines_empty_file():
    # Create an empty test file
    test_file_path = 'tests/empty_test_file.txt'
    open(test_file_path, 'w').close()
    
    # Read the file
    lines = read_file_lines(test_file_path)
    
    # Check the content
    assert lines == []
    
    # Clean up
    os.remove(test_file_path)

def test_read_file_lines_nonexistent_file():
    # Test reading a non-existent file
    with pytest.raises(FileNotFoundError):
        read_file_lines('non_existent_file.txt')

def test_read_file_lines_with_newline_characters():
    # Create a test file with various newline characters
    test_file_path = 'tests/newline_test_file.txt'
    with open(test_file_path, 'w') as f:
        f.write("Line1\nLine2\r\nLine3\r")
    
    # Read the file
    lines = read_file_lines(test_file_path)
    
    # Check the content
    assert lines == ['Line1', 'Line2', 'Line3']
    
    # Clean up
    os.remove(test_file_path)