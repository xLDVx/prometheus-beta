import pytest
import random
from src.random_integer_generator import generate_random_integer

def test_random_integer_basic_functionality():
    """Test that the function generates integers within the specified range."""
    for _ in range(100):  # Multiple runs to ensure randomness
        result = generate_random_integer(1, 10)
        assert 1 <= result <= 10, f"Result {result} is not within range 1-10"

def test_random_integer_single_value_range():
    """Test generating a random integer when min and max are the same."""
    result = generate_random_integer(5, 5)
    assert result == 5, "Should return the same value when min and max are equal"

def test_random_integer_negative_range():
    """Test generating a random integer with negative numbers."""
    for _ in range(100):
        result = generate_random_integer(-10, 10)
        assert -10 <= result <= 10, f"Result {result} is not within range -10-10"

def test_random_integer_invalid_type_inputs():
    """Test that TypeError is raised for non-integer inputs."""
    with pytest.raises(TypeError, match="Both min_value and max_value must be integers"):
        generate_random_integer(1.5, 10)
    
    with pytest.raises(TypeError, match="Both min_value and max_value must be integers"):
        generate_random_integer(1, "10")

def test_random_integer_invalid_range():
    """Test that ValueError is raised when min_value > max_value."""
    with pytest.raises(ValueError, match="min_value must be less than or equal to max_value"):
        generate_random_integer(10, 5)

def test_randomness():
    """Probabilistic test to ensure some level of randomness."""
    results = set(generate_random_integer(1, 10) for _ in range(1000))
    assert len(results) > 1, "Generated numbers do not show sufficient randomness"