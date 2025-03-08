import pytest
from src.staircase_climber import count_staircase_ways

def test_basic_staircase():
    """Test a basic staircase scenario"""
    assert count_staircase_ways([1, 1, 1]) == 4  # 4 unique climbing ways

def test_single_step_staircase():
    """Test a single step staircase"""
    assert count_staircase_ways([1]) == 1

def test_two_step_staircase():
    """Test a two-step staircase"""
    assert count_staircase_ways([1, 1]) == 2

def test_longer_staircase():
    """Test a longer staircase"""
    assert count_staircase_ways([1, 1, 1, 1]) == 8

def test_invalid_none_input():
    """Test handling of None input"""
    with pytest.raises(ValueError, match="Stair lengths cannot be None"):
        count_staircase_ways(None)

def test_invalid_non_positive_input():
    """Test handling of non-positive integers"""
    with pytest.raises(ValueError, match="All stair lengths must be positive integers"):
        count_staircase_ways([1, 0, 2])
    
    with pytest.raises(ValueError, match="All stair lengths must be positive integers"):
        count_staircase_ways([-1, 1, 2])

def test_complex_staircase():
    """Test a more complex staircase with mixed step lengths"""
    assert count_staircase_ways([2, 1, 2]) == 3