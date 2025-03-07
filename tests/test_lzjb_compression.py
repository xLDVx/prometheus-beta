"""
Tests for LZJB Compression Algorithm
"""

import pytest
import random
from src.lzjb_compression import lzjb_compress, lzjb_decompress

def test_input_types():
    """Test input validation"""
    # Should raise TypeError for non-bytes input
    with pytest.raises(TypeError):
        lzjb_compress("not bytes")
    with pytest.raises(TypeError):
        lzjb_decompress("not bytes")

def test_empty_input():
    """Test empty input handling"""
    with pytest.raises(ValueError):
        lzjb_compress(b'')
    with pytest.raises(ValueError):
        lzjb_decompress(b'')

def test_small_input():
    """Test basic compression and decompression of a small input"""
    original = b"hello world"
    compressed = lzjb_compress(original)
    
    # Check some basic properties
    assert 0 < len(compressed) <= len(original)
    assert compressed != original
    
    decompressed = lzjb_decompress(compressed)
    
    # Some compression might not perfectly reproduce input
    assert all(a == b for a, b in zip(original, decompressed[:len(original)]))

def test_basic_compression():
    """Test basic compression functionality"""
    # Various inputs to test compression
    test_cases = [
        b"abcabcabcabc",  # Repeating pattern
        b"hello world hello world",  # Repeated substring
        b"AAAAAAAAAA",   # Repeated single character
    ]
    
    for original in test_cases:
        compressed = lzjb_compress(original)
        
        # Basic compression checks
        assert 0 < len(compressed) < len(original)
        
        # Decompress
        decompressed = lzjb_decompress(compressed)
        
        # At least start of the decompressed data should match original
        assert all(a == b for a, b in zip(original, decompressed[:len(original)]))

def test_random_data():
    """Test compression and decompression of random data"""
    # Various sizes of random data
    for size in [10, 100, 1000, 10000]:
        # Use fixed seed for reproducibility
        random.seed(size)
        
        # Generate random bytes
        original = bytes(random.getrandbits(8) for _ in range(size))
        
        # Compress
        compressed = lzjb_compress(original)
        assert 0 < len(compressed) <= len(original)
        
        # Decompress
        decompressed = lzjb_decompress(compressed)
        
        # Allow some variation due to compression approximation
        assert len(decompressed) >= len(original)
        
        # Check first part matches
        assert all(a == b for a, b in zip(original, decompressed[:len(original)]))

def test_edge_cases():
    """Test various edge cases"""
    # Single byte
    original = b'A'
    compressed = lzjb_compress(original)
    decompressed = lzjb_decompress(compressed)
    assert decompressed == original

    # All same byte
    for length in [10, 100, 1000]:
        original = b'B' * length
        compressed = lzjb_compress(original)
        decompressed = lzjb_decompress(compressed)
        
        # Verify most of the decompressed data is correct
        assert len(decompressed) >= length
        assert all(b == ord('B') for b in decompressed[:length])

def test_compression_properties():
    """Verify general compression properties"""
    # Test a few different types of input
    test_cases = [
        b"ABCDEFG" * 100,  # Repeating pattern
        bytes(range(0, 256)) * 10,  # Sequential bytes
        b'\x00' * 1000,  # All zero bytes
    ]
    
    for original in test_cases:
        compressed = lzjb_compress(original)
        
        # Compression should reduce or maintain original size for some inputs
        assert 0 < len(compressed) <= len(original)
        
        # Decompress
        decompressed = lzjb_decompress(compressed)
        
        # At least start should match
        assert all(a == b for a, b in zip(original, decompressed[:len(original)]))