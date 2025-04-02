import pytest
import sys
import os
import brotli

# Add the src directory to the Python path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'src')))

from brotli_compression import compress_brotli, decompress_brotli

def test_compress_decompress_string():
    """Test compression and decompression of a string"""
    original_text = "Hello, world! This is a test of Brotli compression."
    compressed = compress_brotli(original_text)
    assert compressed != original_text.encode('utf-8')
    
    decompressed = decompress_brotli(compressed)
    assert decompressed.decode('utf-8') == original_text

def test_compress_decompress_bytes():
    """Test compression and decompression of bytes"""
    original_bytes = b'\x00\x01\x02\x03\x04'
    compressed = compress_brotli(original_bytes)
    assert compressed != original_bytes
    
    decompressed = decompress_brotli(compressed)
    assert decompressed == original_bytes

def test_compression_quality():
    """Test different compression qualities"""
    text = "Test compression quality" * 100
    
    # Test various quality levels
    compressed_low = compress_brotli(text, quality=1)
    compressed_high = compress_brotli(text, quality=11)
    
    # High quality should generally result in smaller compressed size
    assert len(compressed_high) <= len(compressed_low)

def test_compression_modes():
    """Test different compression modes"""
    text = "This is a test text for different Brotli modes."
    
    # Verify different modes can compress the same input differently
    def compression_diff_by_mode(first_mode, second_mode):
        """Helper function to check if compressions differ"""
        first_compressed = compress_brotli(text, mode=first_mode)
        second_compressed = compress_brotli(text, mode=second_mode)
        return first_compressed != second_compressed
    
    # Test different mode combinations
    assert compression_diff_by_mode(brotli.MODE_GENERIC, brotli.MODE_TEXT)
    assert compression_diff_by_mode(brotli.MODE_GENERIC, brotli.MODE_FONT)
    assert compression_diff_by_mode(brotli.MODE_TEXT, brotli.MODE_FONT)

def test_invalid_input_types():
    """Test error handling for invalid input types"""
    with pytest.raises(TypeError):
        compress_brotli(123)
    
    with pytest.raises(TypeError):
        decompress_brotli("not bytes")

def test_invalid_compression_quality():
    """Test error handling for invalid compression quality"""
    with pytest.raises(ValueError):
        compress_brotli("test", quality=-1)
    
    with pytest.raises(ValueError):
        compress_brotli("test", quality=12)

def test_invalid_compression_mode():
    """Test error handling for invalid compression mode"""
    with pytest.raises(ValueError):
        compress_brotli("test", mode=999)

def test_empty_input():
    """Test compression and decompression of empty input"""
    empty_string = ""
    empty_bytes = b''
    
    compressed_string = compress_brotli(empty_string)
    compressed_bytes = compress_brotli(empty_bytes)
    
    assert decompress_brotli(compressed_string) == b''
    assert decompress_brotli(compressed_bytes) == b''

def test_large_input():
    """Test compression of a large input"""
    large_text = "This is a large text " * 10000
    
    compressed = compress_brotli(large_text)
    decompressed = decompress_brotli(compressed)
    
    assert decompressed.decode('utf-8') == large_text

def test_decompression_corrupted_data():
    """Test decompression of corrupted data"""
    with pytest.raises(RuntimeError):
        decompress_brotli(b'corrupted_data')