import os
import pytest
import shutil
import tempfile

from src.file_renamer import rename_file

@pytest.fixture
def temp_dir():
    """Create a temporary directory for test files."""
    with tempfile.TemporaryDirectory() as tmpdir:
        yield tmpdir

def test_rename_file_success(temp_dir):
    """Test successful file renaming."""
    # Create a source file
    source_path = os.path.join(temp_dir, 'source.txt')
    dest_path = os.path.join(temp_dir, 'destination.txt')
    
    with open(source_path, 'w') as f:
        f.write('test content')
    
    # Rename the file
    result = rename_file(source_path, dest_path)
    
    # Verify
    assert result == dest_path
    assert not os.path.exists(source_path)
    assert os.path.exists(dest_path)

def test_rename_file_nonexistent_source(temp_dir):
    """Test renaming a non-existent file raises FileNotFoundError."""
    source_path = os.path.join(temp_dir, 'nonexistent.txt')
    dest_path = os.path.join(temp_dir, 'destination.txt')
    
    with pytest.raises(FileNotFoundError):
        rename_file(source_path, dest_path)

def test_rename_file_destination_exists(temp_dir):
    """Test renaming to an existing file raises FileExistsError."""
    # Create source and destination files
    source_path = os.path.join(temp_dir, 'source.txt')
    dest_path = os.path.join(temp_dir, 'destination.txt')
    
    with open(source_path, 'w') as f:
        f.write('source content')
    
    with open(dest_path, 'w') as f:
        f.write('destination content')
    
    # Attempt to rename
    with pytest.raises(FileExistsError):
        rename_file(source_path, dest_path)

def test_rename_file_invalid_input_types():
    """Test that non-string inputs raise TypeError."""
    with pytest.raises(TypeError):
        rename_file(123, 'dest')
    
    with pytest.raises(TypeError):
        rename_file('source', 456)

def test_rename_file_directory_as_source(temp_dir):
    """Test that attempting to rename a directory raises ValueError."""
    source_dir = os.path.join(temp_dir, 'source_dir')
    os.makedirs(source_dir)
    dest_path = os.path.join(temp_dir, 'destination.txt')
    
    with pytest.raises(ValueError):
        rename_file(source_dir, dest_path)

def test_rename_file_across_directories(temp_dir):
    """Test renaming a file across different directories."""
    # Create source file
    source_path = os.path.join(temp_dir, 'source.txt')
    dest_dir = os.path.join(temp_dir, 'new_directory')
    dest_path = os.path.join(dest_dir, 'destination.txt')
    
    with open(source_path, 'w') as f:
        f.write('test content')
    
    # Rename the file
    result = rename_file(source_path, dest_path)
    
    # Verify
    assert result == dest_path
    assert not os.path.exists(source_path)
    assert os.path.exists(dest_path)