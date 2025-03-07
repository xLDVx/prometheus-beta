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
    assert len(compressed) > 0
    assert compressed != original
    
    decompressed = lzjb_decompress(compressed)
    assert len(decompressed) == len(original)

def test_repeated_pattern():
    """Test compression of repeated patterns"""
    original = b"ABCDEFG" * 100
    compressed = lzjb_compress(original)
    
    # Check basic compression properties
    assert len(compressed) < len(original)
    
    # Decompress and verify length
    decompressed = lzjb_decompress(compressed)
    assert len(decompressed) == len(original)

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
        assert len(compressed) > 0
        
        # Decompress
        decompressed = lzjb_decompress(compressed)
        
        # Verify basic properties
        assert len(decompressed) == len(original)

def test_compression_efficiency():
    """Verify compression reduces data size for repetitive data"""
    # Repeated pattern
    original = b"ABCDEFG" * 1000
    compressed = lzjb_compress(original)
    
    # Reasonable compression should happen
    assert len(compressed) < len(original) * 0.5
    
    # Decompress and verify length
    decompressed = lzjb_decompress(compressed)
    assert len(decompressed) == len(original)

def test_edge_cases():
    """Test various edge cases"""
    # Single byte
    original = b'A'
    compressed = lzjb_compress(original)
    decompressed = lzjb_decompress(compressed)
    assert decompressed == original

    # All same byte
    original = b'B' * 1000
    compressed = lzjb_compress(original)
    decompressed = lzjb_decompress(compressed)
    assert decompressed == original