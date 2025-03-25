import pytest
import sys
import os

# Add the src directory to the Python path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'src')))

from huffman_coding import huffman_encode, huffman_decode

def test_huffman_encode_decode():
    """Test full encode and decode process."""
    # Test with various inputs
    test_cases = [
        "hello world",
        "aaaabbbcccddd",
        "abcdefg",
        "   spaces   ",
        "12345"
    ]
    
    for test_input in test_cases:
        # Encode
        encoded_data, huffman_tree = huffman_encode(test_input)
        
        # Decode
        decoded_data = huffman_decode(encoded_data, huffman_tree)
        
        # Verify
        assert decoded_data == test_input

def test_encode_edge_cases():
    """Test edge cases for encoding."""
    # Empty string
    with pytest.raises(ValueError):
        huffman_encode("")
    
    # Single character repeated
    single_char_input = "aaaaa"
    encoded, tree = huffman_encode(single_char_input)
    decoded = huffman_decode(encoded, tree)
    assert decoded == single_char_input

def test_decode_edge_cases():
    """Test edge cases for decoding."""
    # Invalid encoded data
    with pytest.raises(ValueError):
        huffman_decode("", None)
    
    # Empty tree
    with pytest.raises(ValueError):
        huffman_decode("", None)

def test_unique_codes():
    """Ensure unique codes for each character."""
    test_input = "abracadabra"
    encoded, huffman_tree = huffman_encode(test_input)
    
    decoded_data = huffman_decode(encoded, huffman_tree)
    assert decoded_data == test_input