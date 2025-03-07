import os
import pytest
import tempfile
import shutil

from src.file_splitter import split_file

def create_test_file(size):
    """Create a temporary test file with specified size."""
    with tempfile.NamedTemporaryFile(delete=False) as temp_file:
        temp_file.write(b'A' * size)
        return temp_file.name

def test_split_file_basic():
    """Test basic file splitting functionality."""
    # Create a test file
    file_path = create_test_file(1000)
    
    try:
        # Split the file
        chunk_files = split_file(file_path, chunk_size=100)
        
        # Verify chunks
        assert len(chunk_files) == 10
        
        # Verify chunk sizes
        for chunk_file in chunk_files:
            assert os.path.getsize(chunk_file) == 100
        
        # Clean up chunks
        for chunk_file in chunk_files:
            os.remove(chunk_file)
    
    finally:
        # Remove the original test file
        os.remove(file_path)

def test_split_file_custom_output_dir():
    """Test splitting file to a custom output directory."""
    # Create a test file
    file_path = create_test_file(500)
    
    try:
        # Create a temporary output directory
        with tempfile.TemporaryDirectory() as temp_dir:
            # Split the file to custom directory
            chunk_files = split_file(file_path, chunk_size=100, output_dir=temp_dir)
            
            # Verify chunks
            assert len(chunk_files) == 5
            
            # Verify chunk locations
            for chunk_file in chunk_files:
                assert chunk_file.startswith(temp_dir)
                assert os.path.getsize(chunk_file) == 100
    
    finally:
        # Remove the original test file
        os.remove(file_path)

def test_split_file_uneven_last_chunk():
    """Test that the last chunk can be smaller."""
    # Create a test file
    file_path = create_test_file(1234)
    
    try:
        # Split the file
        chunk_files = split_file(file_path, chunk_size=500)
        
        # Verify chunks
        assert len(chunk_files) == 3
        
        # Verify chunk sizes
        assert os.path.getsize(chunk_files[0]) == 500
        assert os.path.getsize(chunk_files[1]) == 500
        assert os.path.getsize(chunk_files[2]) <= 500
    
    finally:
        # Remove the original test file
        os.remove(file_path)

def test_split_file_invalid_chunk_size():
    """Test error handling for invalid chunk size."""
    # Create a test file
    file_path = create_test_file(100)
    
    try:
        # Attempt to split with invalid chunk size
        with pytest.raises(ValueError, match="Chunk size must be a positive integer"):
            split_file(file_path, chunk_size=0)
        
        with pytest.raises(ValueError, match="Chunk size must be a positive integer"):
            split_file(file_path, chunk_size=-10)
    
    finally:
        # Remove the original test file
        os.remove(file_path)

def test_split_file_nonexistent_file():
    """Test error handling for nonexistent file."""
    with pytest.raises(FileNotFoundError):
        split_file("/path/to/nonexistent/file.txt", chunk_size=100)

def test_empty_file():
    """Test splitting an empty file."""
    # Create an empty test file
    with tempfile.NamedTemporaryFile(delete=False) as temp_file:
        file_path = temp_file.name
    
    try:
        # Split the empty file
        chunk_files = split_file(file_path, chunk_size=100)
        
        # Verify no chunks created
        assert len(chunk_files) == 0
    
    finally:
        # Remove the test file
        os.remove(file_path)