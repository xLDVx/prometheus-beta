import pytest
from src.triangle_sequence import generate_triangle_sequence

def test_generate_triangle_sequence_basic():
    """Test generating first few triangle numbers."""
    assert generate_triangle_sequence(0) == []
    assert generate_triangle_sequence(1) == [1]
    assert generate_triangle_sequence(5) == [1, 3, 6, 10, 15]

def test_generate_triangle_sequence_edge_cases():
    """Test edge cases for input validation."""
    # Test zero input
    assert generate_triangle_sequence(0) == []
    
    # Test input type errors
    with pytest.raises(TypeError, match="Input must be an integer"):
        generate_triangle_sequence(3.14)
    
    with pytest.raises(TypeError, match="Input must be an integer"):
        generate_triangle_sequence("5")
    
    # Test negative input
    with pytest.raises(ValueError, match="Number of triangle numbers must be non-negative"):
        generate_triangle_sequence(-1)

def test_generate_triangle_sequence_large_input():
    """Test generating a larger sequence."""
    sequence = generate_triangle_sequence(10)
    assert len(sequence) == 10
    
    # Verify the 10th triangle number is correct (1+2+3+4+5+6+7+8+9+10)
    assert sequence[-1] == 55