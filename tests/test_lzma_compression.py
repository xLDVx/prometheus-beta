import pytest
import sys
import os

# Add the src directory to the Python path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'src')))

from lzma_compression import lzma_compress, lzma_decompress

def test_lzma_compress_and_decompress_bytes():
    """Test compression and decompression of bytes data."""
    original_data = b'Hello, this is a test of LZMA compression!'
    compressed = lzma_compress(original_data)
    assert compressed != original_data
    assert len(compressed) > 0
    
    decompressed = lzma_decompress(compressed)
    assert decompressed == original_data

def test_lzma_compress_and_decompress_string():
    """Test compression and decompression of string data."""
    original_data = 'Hello, this is a test of LZMA compression!'
    compressed = lzma_compress(original_data)
    assert compressed != original_data.encode('utf-8')
    assert len(compressed) > 0
    
    decompressed = lzma_decompress(compressed)
    assert decompressed == original_data.encode('utf-8')

def test_lzma_compress_empty_input():
    """Test handling of empty input."""
    with pytest.raises(ValueError, match="Input data cannot be empty"):
        lzma_compress(b'')
    
    with pytest.raises(ValueError, match="Input data cannot be empty"):
        lzma_compress('')

def test_lzma_decompress_empty_input():
    """Test handling of empty compressed input."""
    with pytest.raises(ValueError, match="Compressed data cannot be empty"):
        lzma_decompress(b'')

def test_lzma_compress_invalid_type():
    """Test handling of invalid input types."""
    with pytest.raises(TypeError, match="Input must be bytes or str"):
        lzma_compress(123)
    
    with pytest.raises(TypeError, match="Input must be bytes or str"):
        lzma_compress(["list"])

def test_lzma_decompress_invalid_type():
    """Test handling of invalid compressed data types."""
    with pytest.raises(TypeError, match="Compressed data must be bytes"):
        lzma_decompress('not bytes')
    
    with pytest.raises(TypeError, match="Compressed data must be bytes"):
        lzma_decompress(123)

def test_lzma_large_data():
    """Test compression and decompression of large data."""
    large_data = b'A' * 100000
    compressed = lzma_compress(large_data)
    assert len(compressed) < len(large_data)
    
    decompressed = lzma_decompress(compressed)
    assert decompressed == large_data