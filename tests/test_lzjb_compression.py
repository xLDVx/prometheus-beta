"""
Tests for LZJB Compression Algorithm
"""

import pytest
import random
import string
from src.lzjb_compression import lzjb_compress, lzjb_decompress

def test_compress_decompress_simple():
    """Test basic compression and decompression of a simple string"""
    original = b"hello world hello world"
    compressed = lzjb_compress(original)
    assert compressed != original
    decompressed = lzjb_decompress(compressed)
    assert decompressed == original

def test_compress_decompress_random():
    """Test compression and decompression of random data"""
    # Generate random bytes
    random.seed(42)  # For reproducibility
    original = bytes(random.getrandbits(8) for _ in range(1000))
    compressed = lzjb_compress(original)
    decompressed = lzjb_decompress(compressed)
    assert decompressed == original

def test_repeated_pattern():
    """Test compression of repeated patterns"""
    original = b"ABCABCABCABCABCABCABCABC" * 10
    compressed = lzjb_compress(original)
    assert len(compressed) < len(original)
    decompressed = lzjb_decompress(compressed)
    assert decompressed == original

def test_edge_cases():
    """Test edge cases for compression and decompression"""
    # Single byte
    single_byte = b'A'
    compressed = lzjb_compress(single_byte)
    decompressed = lzjb_decompress(compressed)
    assert decompressed == single_byte

    # Empty input raises ValueError
    with pytest.raises(ValueError):
        lzjb_compress(b'')
    with pytest.raises(ValueError):
        lzjb_decompress(b'')

def test_invalid_input_types():
    """Test error handling for invalid input types"""
    # Non-bytes input should raise TypeError
    with pytest.raises(TypeError):
        lzjb_compress("not bytes")
    with pytest.raises(TypeError):
        lzjb_decompress("not bytes")

def test_large_input():
    """Test compression and decompression of larger input"""
    # Generate a larger random input
    random.seed(123)  # For reproducibility
    large_input = bytes(random.getrandbits(8) for _ in range(10000))
    compressed = lzjb_compress(large_input)
    decompressed = lzjb_decompress(compressed)
    assert decompressed == large_input

def test_compression_efficiency():
    """Verify that compression reduces data size"""
    # Repeated pattern should compress well
    original = b"ABCDEFG" * 1000
    compressed = lzjb_compress(original)
    assert len(compressed) < len(original)
    decompressed = lzjb_decompress(compressed)
    assert decompressed == original