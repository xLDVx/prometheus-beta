import pytest
from src.bit_reversal import reverse_bits

def test_reverse_bits_standard_cases():
    """Test standard bit reversal scenarios."""
    # Example from problem statement
    assert reverse_bits(43261596) == 964176192
    
    # All 1s case
    assert reverse_bits(0b11111111111111111111111111111111) == 0b11111111111111111111111111111111
    
    # All 0s case
    assert reverse_bits(0) == 0

def test_reverse_bits_edge_cases():
    """Test edge cases for bit reversal."""
    # Maximum 32-bit unsigned integer
    max_32bit = 0xFFFFFFFF
    assert reverse_bits(max_32bit) == max_32bit
    
    # Powers of 2
    assert reverse_bits(1) == 0x80000000  # 1 becomes 2^31
    assert reverse_bits(2) == 0x40000000  # 2 becomes 2^30

def test_reverse_bits_invalid_input():
    """Test error handling for invalid inputs."""
    # Negative number
    with pytest.raises(ValueError, match="Input must be a 32-bit unsigned integer"):
        reverse_bits(-1)
    
    # Number larger than 32-bit unsigned int
    with pytest.raises(ValueError, match="Input must be a 32-bit unsigned integer"):
        reverse_bits(0x100000000)
    
    # Non-integer input
    with pytest.raises(ValueError, match="Input must be a 32-bit unsigned integer"):
        reverse_bits("not an integer")
    with pytest.raises(ValueError, match="Input must be a 32-bit unsigned integer"):
        reverse_bits(3.14)