import os
import pytest
import tempfile
import shutil

from src.list_subdirectories import list_subdirectories

def test_list_subdirectories_normal_case():
    """Test listing subdirectories in a normal scenario."""
    with tempfile.TemporaryDirectory() as temp_dir:
        # Create some subdirectories
        os.mkdir(os.path.join(temp_dir, 'subdir1'))
        os.mkdir(os.path.join(temp_dir, 'subdir2'))
        os.mkdir(os.path.join(temp_dir, 'subdir3'))
        
        # Create a file to ensure only directories are returned
        with open(os.path.join(temp_dir, 'somefile.txt'), 'w') as f:
            f.write('test')
        
        # Get subdirectories
        result = list_subdirectories(temp_dir)
        
        # Assert
        assert set(result) == {'subdir1', 'subdir2', 'subdir3'}
        assert len(result) == 3

def test_list_subdirectories_empty_directory():
    """Test listing subdirectories in an empty directory."""
    with tempfile.TemporaryDirectory() as temp_dir:
        result = list_subdirectories(temp_dir)
        assert result == []

def test_list_subdirectories_nonexistent_directory():
    """Test that FileNotFoundError is raised for nonexistent directory."""
    with tempfile.TemporaryDirectory() as temp_dir:
        nonexistent_path = os.path.join(temp_dir, 'nonexistent_dir')
        with pytest.raises(FileNotFoundError):
            list_subdirectories(nonexistent_path)

def test_list_subdirectories_not_a_directory():
    """Test that NotADirectoryError is raised when path is not a directory."""
    with tempfile.TemporaryDirectory() as temp_dir:
        # Create a file
        file_path = os.path.join(temp_dir, 'testfile.txt')
        with open(file_path, 'w') as f:
            f.write('test')
        
        with pytest.raises(NotADirectoryError):
            list_subdirectories(file_path)

def test_list_subdirectories_sorted():
    """Test that subdirectories are returned in sorted order."""
    with tempfile.TemporaryDirectory() as temp_dir:
        # Create subdirectories in non-alphabetical order
        os.mkdir(os.path.join(temp_dir, 'zebra'))
        os.mkdir(os.path.join(temp_dir, 'apple'))
        os.mkdir(os.path.join(temp_dir, 'banana'))
        
        result = list_subdirectories(temp_dir)
        
        # Assert sorted order
        assert result == ['apple', 'banana', 'zebra']