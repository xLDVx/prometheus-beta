"""
Test suite for LZSS Compression Algorithm.

This module contains comprehensive tests for the LZSSCompressor class,
covering various scenarios and edge cases.
"""

import pytest
import random
import string

from src.lzss_compression import LZSSCompressor

def generate_random_data(length):
    """Generate random bytes of specified length."""
    return ''.join(random.choice(string.ascii_letters + string.digits) 
                   for _ in range(length)).encode('utf-8')

def test_compression_basic():
    """Test basic compression and decompression."""
    compressor = LZSSCompressor()
    test_data = b"HELLO WORLD HELLO WORLD"
    
    compressed = compressor.compress(test_data)
    decompressed = compressor.decompress(compressed)
    
    assert decompressed == test_data

def test_repeated_pattern():
    """Test compression of data with repeated patterns."""
    compressor = LZSSCompressor()
    test_data = b"ABCABCABCABCABCABC" * 10
    
    compressed = compressor.compress(test_data)
    decompressed = compressor.decompress(compressed)
    
    assert decompressed == test_data

def test_random_data():
    """Test compression and decompression of random data."""
    compressor = LZSSCompressor()
    test_data = generate_random_data(1000)
    
    compressed = compressor.compress(test_data)
    decompressed = compressor.decompress(compressed)
    
    assert decompressed == test_data

def test_empty_input():
    """Test handling of empty input."""
    compressor = LZSSCompressor()
    
    with pytest.raises(ValueError, match="Input data cannot be empty"):
        compressor.compress(b"")
    
    with pytest.raises(ValueError, match="Compressed data cannot be empty"):
        compressor.decompress(b"")

def test_malformed_compressed_data():
    """Test handling of malformed compressed data."""
    compressor = LZSSCompressor()
    
    # Incomplete compressed data
    with pytest.raises(ValueError, match="Malformed compressed data"):
        compressor.decompress(b'\x00\x01')
    
    # Invalid flag
    with pytest.raises(ValueError, match="Invalid flag"):
        compressor.decompress(b'\x02\x01')

def test_input_type_validation():
    """Test input type validation."""
    compressor = LZSSCompressor()
    
    # Test string input for compression
    test_data = "Hello, World!"
    compressed = compressor.compress(test_data)
    decompressed = compressor.decompress(compressed)
    assert decompressed == test_data.encode('utf-8')
    
    # Test non-bytes input for decompression
    with pytest.raises(TypeError, match="Input must be bytes"):
        compressor.decompress("not bytes")

def test_custom_window_size():
    """Test compression with custom window size."""
    compressor = LZSSCompressor(window_size=128, min_match_length=2)
    test_data = b"ABCABCABCABCABCABC" * 10
    
    compressed = compressor.compress(test_data)
    decompressed = compressor.decompress(compressed)
    
    assert decompressed == test_data