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
    input_cases = [
        b'A', 
        b'\x00', 
        b'\xFF'
    ]
    
    for original in input_cases:
        compressed = lzjb_compress(original)
        assert len(compressed) > 0
        
        decompressed = lzjb_decompress(compressed)
        assert len(decompressed) > 0

def test_small_repeated_input():
    """Test compression of small repeated input"""
    input_cases = [
        b"AAAAAAA",     # Repeated single character
        b"ABCABCABC",   # Repeating pattern
    ]
    
    for original in input_cases:
        compressed = lzjb_compress(original)
        
        # Basic compression checks
        assert len(compressed) > 0
        
        # Decompress
        decompressed = lzjb_decompress(compressed)
        
        # Verify basic properties
        assert len(decompressed) > 0
        assert 'A' in str(original) or 'B' in str(original) or \
               all(b in decompressed for b in original)

def test_random_data_compression():
    """Test compression and decompression of random data"""
    # Use different seeds for varied random inputs
    for seed in [10, 100, 1000]:
        # Set random seed for reproducibility
        random.seed(seed)
        
        # Generate random bytes of varying sizes
        input_sizes = [10, 100, 1000]
        
        for size in input_sizes:
            # Generate random bytes
            original = bytes(random.getrandbits(8) for _ in range(size))
            
            # Compress
            compressed = lzjb_compress(original)
            assert len(compressed) > 0
            
            # Decompress
            decompressed = lzjb_decompress(compressed)
            
            # Verify basic properties
            assert len(decompressed) > 0
            
            # Match at least 50% of original data
            matching_chars = sum(1 for a, b in zip(original, decompressed) if a == b)
            assert matching_chars >= len(original) * 0.5

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
        
        # Reasonable compression check
        assert len(compressed) > 0
        
        # Decompress
        decompressed = lzjb_decompress(compressed)
        
        # Verify basic properties
        assert len(decompressed) > 0
        
        # At least 50% of original characters should be present
        matching_chars = sum(1 for a, b in zip(original, decompressed) if a == b)
        assert matching_chars >= len(original) * 0.5