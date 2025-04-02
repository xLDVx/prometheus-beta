import os
import pytest
import tempfile

from src.file_line_counter import count_file_lines

def test_count_file_lines_normal():
    # Create a temporary file with known number of lines
    with tempfile.NamedTemporaryFile(mode='w', delete=False) as temp_file:
        temp_file.write("Line 1\nLine 2\nLine 3")
        temp_file_path = temp_file.name
    
    try:
        assert count_file_lines(temp_file_path) == 3
    finally:
        # Clean up the temporary file
        os.unlink(temp_file_path)

def test_count_file_lines_empty():
    # Create an empty temporary file
    with tempfile.NamedTemporaryFile(mode='w', delete=False) as temp_file:
        temp_file_path = temp_file.name
    
    try:
        assert count_file_lines(temp_file_path) == 0
    finally:
        # Clean up the temporary file
        os.unlink(temp_file_path)

def test_count_file_lines_single_line():
    # Create a file with a single line
    with tempfile.NamedTemporaryFile(mode='w', delete=False) as temp_file:
        temp_file.write("Single line")
        temp_file_path = temp_file.name
    
    try:
        assert count_file_lines(temp_file_path) == 1
    finally:
        # Clean up the temporary file
        os.unlink(temp_file_path)

def test_count_file_lines_file_not_found():
    # Test for FileNotFoundError
    with pytest.raises(FileNotFoundError):
        count_file_lines("non_existent_file.txt")

def test_count_file_lines_empty_string():
    # Test with empty string path
    with pytest.raises(FileNotFoundError):
        count_file_lines("")