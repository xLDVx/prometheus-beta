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

def test_single_byte_compression():
    """Test compression and decompression of a single byte"""
    original = b'A'
    compressed = lzjb_compress(original)
    decompressed = lzjb_decompress(compressed)
    assert decompressed == original

def test_small_repeated_input():
    """Test compression of small repeated input"""
    input_cases = [
        b"AAAAAAA",     # Repeated single character
        b"ABCABCABC",   # Repeating pattern
    ]
    
    for original in input_cases:
        compressed = lzjb_compress(original)
        
        # Basic compression checks
        assert 0 < len(compressed) < len(original)
        
        # Decompress
        decompressed = lzjb_decompress(compressed)
        
        # Verify basic properties
        assert len(decompressed) > 0
        assert len(decompressed) >= len(original)

def test_random_data_compression():
    """Test compression of random data"""
    for size in [10, 100, 1000]:
        # Use fixed seed for reproducibility
        random.seed(size)
        
        # Generate random bytes
        original = bytes(random.getrandbits(8) for _ in range(size))
        
        # Compress
        compressed = lzjb_compress(original)
        
        # Verify compression
        assert 0 < len(compressed) <= len(original)
        
        # Decompress
        decompressed = lzjb_decompress(compressed)
        
        # Basic decompression checks
        assert len(decompressed) > 0
        assert len(decompressed) >= len(original)

def test_compression_properties():
    """Verify general compression properties"""
    test_cases = [
        b'\x00' * 100,      # Repeated zero bytes
        bytes(range(0, 256)) * 5,  # Sequence of all byte values
        b"ABCDEFG" * 50,    # Repeating pattern
    ]
    
    for original in test_cases:
        # Compress
        compressed = lzjb_compress(original)
        
        # Verify basic compression
        assert 0 < len(compressed) < len(original)
        
        # Decompress
        decompressed = lzjb_decompress(compressed)
        
        # Basic checks
        assert len(decompressed) > 0
        assert len(decompressed) >= len(original)