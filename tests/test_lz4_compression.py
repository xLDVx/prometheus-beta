"""
Test suite for LZ4 compression implementation
"""

import pytest
import sys
import os

# Add the src directory to the Python path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'src')))

from lz4_compression import lz4_compress, lz4_decompress

def test_basic_compression_decompression():
    """Test basic compression and decompression of a simple string"""
    original_data = b"Hello, world! This is a test of LZ4 compression."
    compressed = lz4_compress(original_data)
    decompressed = lz4_decompress(compressed)
    
    assert decompressed == original_data

def test_string_input():
    """Test compression and decompression with string input"""
    original_data = "Hello, world! This is a test of LZ4 compression."
    compressed = lz4_compress(original_data)
    decompressed = lz4_decompress(compressed)
    
    assert decompressed == original_data.encode('utf-8')

def test_repeated_sequence():
    """Test compression of data with repeated sequences"""
    original_data = b"ABCABCABCABCABCABCABC"
    compressed = lz4_compress(original_data)
    decompressed = lz4_decompress(compressed)
    
    assert decompressed == original_data

def test_empty_input_raises_error():
    """Test that empty input raises a ValueError"""
    with pytest.raises(ValueError):
        lz4_compress(b"")
    
    with pytest.raises(ValueError):
        lz4_decompress(b"")

def test_invalid_input_type():
    """Test that invalid input types raise a TypeError"""
    with pytest.raises(TypeError):
        lz4_compress(123)
    
    with pytest.raises(TypeError):
        lz4_decompress(123)

def test_long_input():
    """Test compression and decompression of a longer input"""
    original_data = b"This is a longer test string with some repeated content " * 100
    compressed = lz4_compress(original_data)
    decompressed = lz4_decompress(compressed)
    
    assert decompressed == original_data

def test_binary_data():
    """Test compression of binary data"""
    original_data = bytes([0, 1, 2, 3, 255, 254, 253, 0, 1, 2, 3])
    compressed = lz4_compress(original_data)
    decompressed = lz4_decompress(compressed)
    
    assert decompressed == original_data