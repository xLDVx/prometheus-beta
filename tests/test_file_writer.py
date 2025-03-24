"""
Tests for the file_writer module.
"""

import os
import pytest
import tempfile

from src.file_writer import write_string_to_file

def test_write_string_to_file_successful():
    """Test writing a string to a file successfully."""
    with tempfile.NamedTemporaryFile(mode='w', delete=False) as temp_file:
        temp_path = temp_file.name
    
    test_content = "Hello, world!"
    write_string_to_file(temp_path, test_content)
    
    with open(temp_path, 'r') as file:
        assert file.read() == test_content
    
    # Clean up
    os.unlink(temp_path)

def test_write_string_to_file_empty_string():
    """Test writing an empty string to a file."""
    with tempfile.NamedTemporaryFile(mode='w', delete=False) as temp_file:
        temp_path = temp_file.name
    
    write_string_to_file(temp_path, "")
    
    with open(temp_path, 'r') as file:
        assert file.read() == ""
    
    # Clean up
    os.unlink(temp_path)

def test_write_string_to_file_invalid_filepath_type():
    """Test raising TypeError for non-string filepath."""
    with pytest.raises(TypeError, match="file_path must be a string"):
        write_string_to_file(123, "test content")

def test_write_string_to_file_invalid_content_type():
    """Test raising TypeError for non-string content."""
    with tempfile.NamedTemporaryFile(mode='w', delete=False) as temp_file:
        temp_path = temp_file.name
    
    with pytest.raises(TypeError, match="content must be a string"):
        write_string_to_file(temp_path, 123)
    
    # Clean up
    os.unlink(temp_path)

def test_write_string_to_file_empty_filepath():
    """Test raising ValueError for empty filepath."""
    with pytest.raises(ValueError, match="file_path cannot be an empty string"):
        write_string_to_file("", "test content")

def test_write_string_to_file_unicode_content():
    """Test writing Unicode content to a file."""
    with tempfile.NamedTemporaryFile(mode='w', delete=False) as temp_file:
        temp_path = temp_file.name
    
    unicode_content = "こんにちは世界"
    write_string_to_file(temp_path, unicode_content)
    
    with open(temp_path, 'r', encoding='utf-8') as file:
        assert file.read() == unicode_content
    
    # Clean up
    os.unlink(temp_path)