import pytest
import sys
import os

# Add the src directory to the Python path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'src')))

from huffman_coding import (
    huffman_encode, 
    huffman_decode, 
    build_frequency_dict, 
    build_huffman_tree, 
    build_huffman_codes
)

def test_build_frequency_dict():
    """Test frequency dictionary creation."""
    # Test with normal input
    freq = build_frequency_dict("hello world")
    assert freq == {'h': 1, 'e': 1, 'l': 3, 'o': 2, ' ': 1, 'w': 1, 'r': 1, 'd': 1}
    
    # Test with empty string
    assert build_frequency_dict("") == {}

def test_build_huffman_tree():
    """Test Huffman tree construction."""
    # Test with simple dictionary
    freq_dict = {'a': 5, 'b': 3, 'c': 2}
    tree = build_huffman_tree(freq_dict)
    
    assert tree.freq == 10
    assert tree.char is None
    
    # Test with single character
    single_dict = {'x': 1}
    single_tree = build_huffman_tree(single_dict)
    assert single_tree.char == 'x'
    assert single_tree.freq == 1

    # Test empty dictionary raises error
    with pytest.raises(ValueError):
        build_huffman_tree({})

def test_build_huffman_codes():
    """Test Huffman code generation."""
    # Create a sample tree
    freq_dict = {'a': 5, 'b': 3, 'c': 2}
    tree = build_huffman_tree(freq_dict)
    
    # Generate codes
    codes = build_huffman_codes(tree)
    
    # Verify codes exist
    assert all(char in codes for char in ['a', 'b', 'c'])
    assert len(set(codes.values())) == 3  # Unique codes

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

def test_huffman_encode_edge_cases():
    """Test edge cases for encoding."""
    # Empty string
    with pytest.raises(ValueError):
        huffman_encode("")
    
    # Single character repeated
    single_char_input = "aaaaa"
    encoded, tree = huffman_encode(single_char_input)
    decoded = huffman_decode(encoded, tree)
    assert decoded == single_char_input

def test_huffman_decode_edge_cases():
    """Test edge cases for decoding."""
    # Invalid encoded data
    with pytest.raises(ValueError):
        huffman_decode("", None)
    
    # Empty tree
    with pytest.raises(ValueError):
        huffman_decode("10101", None)

def test_unique_codes():
    """Ensure generated Huffman codes are unique."""
    test_input = "abracadabra"
    _, huffman_tree = huffman_encode(test_input)
    codes = build_huffman_codes(huffman_tree)
    
    # Verify codes are unique
    unique_codes = set(codes.values())
    assert len(unique_codes) == len(codes)