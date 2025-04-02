import pytest
import math
from src.circle_area import calculate_circle_area

def test_circle_area_positive_radius():
    """Test area calculation for positive radii."""
    assert calculate_circle_area(1) == pytest.approx(math.pi)
    assert calculate_circle_area(0) == 0
    assert calculate_circle_area(2.5) == pytest.approx(19.6349540849)

def test_circle_area_edge_cases():
    """Test edge cases for radius."""
    # Test zero radius
    assert calculate_circle_area(0) == 0

def test_circle_area_invalid_inputs():
    """Test invalid input handling."""
    # Test negative radius
    with pytest.raises(ValueError, match="Radius cannot be negative"):
        calculate_circle_area(-1)
    
    # Test non-numeric inputs
    with pytest.raises(TypeError, match="Radius must be a number"):
        calculate_circle_area("2")
    
    with pytest.raises(TypeError, match="Radius must be a number"):
        calculate_circle_area([1])
    
    with pytest.raises(TypeError, match="Radius must be a number"):
        calculate_circle_area(None)