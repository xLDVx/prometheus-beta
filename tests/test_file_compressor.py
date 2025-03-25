import os
import gzip
import pytest
import shutil
import tempfile

from src.file_compressor import compress_file

@pytest.fixture
def temp_file():
    """Create a temporary file for testing."""
    with tempfile.NamedTemporaryFile(mode='w', delete=False) as temp:
        temp.write("This is a test file for compression.")
        temp_path = temp.name
    yield temp_path
    # Cleanup
    if os.path.exists(temp_path):
        os.unlink(temp_path)
    compressed_path = temp_path + '.gz'
    if os.path.exists(compressed_path):
        os.unlink(compressed_path)

def test_compress_file_default_output(temp_file):
    """Test compression with default output path."""
    compressed_path = compress_file(temp_file)
    
    # Verify compressed file exists
    assert os.path.exists(compressed_path)
    assert compressed_path.endswith('.gz')
    
    # Verify file is compressed
    with gzip.open(compressed_path, 'rt') as f:
        content = f.read()
        assert content == "This is a test file for compression."

def test_compress_file_custom_output(temp_file):
    """Test compression with custom output path."""
    custom_output = temp_file + '.custom.gz'
    compressed_path = compress_file(temp_file, custom_output)
    
    # Verify compressed file exists at custom path
    assert os.path.exists(compressed_path)
    assert compressed_path == custom_output
    
    # Verify file is compressed
    with gzip.open(compressed_path, 'rt') as f:
        content = f.read()
        assert content == "This is a test file for compression."

def test_compress_nonexistent_file():
    """Test compressing a non-existent file raises FileNotFoundError."""
    with pytest.raises(FileNotFoundError):
        compress_file('/path/to/nonexistent/file.txt')

def test_compress_directory():
    """Test compressing a directory raises IsADirectoryError."""
    with pytest.raises(IsADirectoryError):
        compress_file(tempfile.gettempdir())

def test_compress_large_file():
    """Test compressing a larger file."""
    with tempfile.NamedTemporaryFile(mode='w', delete=False) as temp:
        # Create a larger file
        temp.write("x" * 1_000_000)  # 1 MB of data
        temp_path = temp.name
    
    try:
        compressed_path = compress_file(temp_path)
        
        # Verify compression
        assert os.path.exists(compressed_path)
        assert os.path.getsize(compressed_path) < os.path.getsize(temp_path)
    finally:
        # Cleanup
        if os.path.exists(temp_path):
            os.unlink(temp_path)
        compressed_path = temp_path + '.gz'
        if os.path.exists(compressed_path):
            os.unlink(compressed_path)