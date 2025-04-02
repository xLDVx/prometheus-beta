import pytest
import sys
import os

# Ensure src directory is in Python path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'src')))

from lzc_compression import lzc_compress, lzc_decompress

def test_lzc_compression_basic():
    """Test basic compression and decompression of simple data"""
    original = b'AAAAABBBBB'
    compressed = lzc_compress(original)
    decompressed = lzc_decompress(compressed)
    assert decompressed == original

def test_lzc_compression_random_data():
    """Test compression and decompression of random data"""
    original = b'Hello, world! This is a test of LZC compression.'
    compressed = lzc_compress(original)
    decompressed = lzc_decompress(compressed)
    assert decompressed == original

def test_lzc_compression_repeated_patterns():
    """Test compression of data with repeated patterns"""
    original = b'abcabcabcabcabcabc'
    compressed = lzc_compress(original)
    decompressed = lzc_decompress(compressed)
    assert decompressed == original

def test_lzc_compression_empty_input():
    """Test error handling for empty input"""
    with pytest.raises(ValueError, match="Input data cannot be empty"):
        lzc_compress(b'')
    with pytest.raises(ValueError, match="Compressed data cannot be empty"):
        lzc_decompress([])

def test_lzc_compression_invalid_input_type():
    """Test error handling for invalid input types"""
    with pytest.raises(TypeError, match="Input must be bytes or bytearray"):
        lzc_compress("not bytes")
    with pytest.raises(TypeError, match="Input must be a list of integer codes"):
        lzc_decompress("not a list")

def test_lzc_compression_single_byte():
    """Test compression and decompression of a single byte"""
    original = b'A'
    compressed = lzc_compress(original)
    decompressed = lzc_decompress(compressed)
    assert decompressed == original

def test_lzc_compression_large_input():
    """Test compression and decompression of larger input"""
    original = b'0' * 1000
    compressed = lzc_compress(original)
    decompressed = lzc_decompress(compressed)
    assert decompressed == original

def test_lzc_compression_binary_data():
    """Test compression of binary data with various byte values"""
    original = bytes(range(256)) * 3
    compressed = lzc_compress(original)
    decompressed = lzc_decompress(compressed)
    assert decompressed == original