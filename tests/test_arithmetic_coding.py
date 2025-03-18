"""
Test suite for Arithmetic Coding implementation
"""

import pytest
import math
from src.arithmetic_coding import arithmetic_encode, arithmetic_decode


def test_basic_encoding():
    """Test basic encoding of a simple string"""
    data = "hello"
    result = arithmetic_encode(data)
    
    # Check returned dictionary structure
    assert 'compressed_value' in result
    assert 'probabilities' in result
    
    # Verify probabilities
    probs = result['probabilities']
    assert len(probs) > 0
    assert all('frequency' in p and 'probability' in p and 'low' in p and 'high' in p for p in probs.values())


def test_basic_encoding_decoding():
    """Test end-to-end encoding and decoding"""
    original_data = "hello world"
    
    # Encode
    encoded = arithmetic_encode(original_data)
    compressed_value = encoded['compressed_value']
    probabilities = encoded['probabilities']
    
    # Decode
    decoded = arithmetic_decode(compressed_value, probabilities, len(original_data))
    
    assert decoded == original_data


def test_empty_input_error():
    """Test error handling for empty input"""
    with pytest.raises(ValueError):
        arithmetic_encode("")
    
    with pytest.raises(ValueError):
        arithmetic_decode(0.5, {}, 0)


def test_single_character_input():
    """Test encoding and decoding of a single character"""
    data = "a"
    encoded = arithmetic_encode(data)
    decoded = arithmetic_decode(
        encoded['compressed_value'], 
        encoded['probabilities'], 
        len(data)
    )
    assert decoded == data


def test_repeated_characters():
    """Test encoding and decoding of repeated characters"""
    data = "aaaa"
    encoded = arithmetic_encode(data)
    decoded = arithmetic_decode(
        encoded['compressed_value'], 
        encoded['probabilities'], 
        len(data)
    )
    assert decoded == data


def test_compressed_value_range():
    """Verify that compressed value is always between 0 and 1"""
    data = "test string"
    encoded = arithmetic_encode(data)
    compressed = encoded['compressed_value']
    
    assert 0 <= compressed <= 1, "Compressed value must be between 0 and 1"


def test_probability_distribution():
    """Verify probability distribution calculation"""
    data = "hello"
    encoded = arithmetic_encode(data)
    probs = encoded['probabilities']
    
    # Check that probabilities sum to approximately 1
    total_prob = sum(prob['probability'] for prob in probs.values())
    assert math.isclose(total_prob, 1.0, rel_tol=1e-9), "Probabilities must sum to 1"