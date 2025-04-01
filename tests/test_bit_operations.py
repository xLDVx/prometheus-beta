import pytest
from src.bit_operations import count_set_bits

def test_count_set_bits_positive_numbers():
    """Test counting set bits for positive integers."""
    assert count_set_bits(0) == 0
    assert count_set_bits(1) == 1
    assert count_set_bits(7) == 3  # 111 in binary
    assert count_set_bits(15) == 4  # 1111 in binary
    assert count_set_bits(255) == 8  # 11111111 in binary

def test_count_set_bits_negative_numbers():
    """Test counting set bits for negative integers."""
    assert count_set_bits(-1) == 1
    assert count_set_bits(-7) == 3
    assert count_set_bits(-15) == 4

def test_count_set_bits_large_numbers():
    """Test counting set bits for large integers."""
    assert count_set_bits(1024) == 1
    assert count_set_bits(2**20 - 1) == 20

def test_count_set_bits_error_handling():
    """Test error handling for invalid input types."""
    with pytest.raises(TypeError):
        count_set_bits("not an integer")
    
    with pytest.raises(TypeError):
        count_set_bits(3.14)
    
    with pytest.raises(TypeError):
        count_set_bits(None)