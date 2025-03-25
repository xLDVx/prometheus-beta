import pytest
from src.knapsack_solver import solve_knapsack

def test_basic_knapsack():
    """Test a basic knapsack scenario"""
    items = [(2, 3), (3, 4), (4, 5), (5, 6)]
    max_weight = 10
    max_value, selected = solve_knapsack(items, max_weight)
    assert max_value == 13
    assert set(selected) == {1, 2}

def test_empty_items():
    """Test with empty items list"""
    items = []
    max_weight = 10
    max_value, selected = solve_knapsack(items, max_weight)
    assert max_value == 0
    assert selected == []

def test_zero_capacity():
    """Test with zero weight capacity"""
    items = [(2, 3), (3, 4), (4, 5)]
    max_weight = 0
    max_value, selected = solve_knapsack(items, max_weight)
    assert max_value == 0
    assert selected == []

def test_single_item_fits():
    """Test when a single item fits perfectly"""
    items = [(5, 10), (3, 7), (2, 4)]
    max_weight = 5
    max_value, selected = solve_knapsack(items, max_weight)
    assert max_value == 10
    assert selected == [0]

def test_large_capacity():
    """Test with capacity larger than total item weights"""
    items = [(2, 3), (3, 4), (4, 5)]
    max_weight = 20
    max_value, selected = solve_knapsack(items, max_weight)
    assert max_value == 12
    assert set(selected) == {0, 1, 2}

def test_complex_scenario():
    """Test a more complex knapsack scenario"""
    items = [(10, 60), (20, 100), (30, 120)]
    max_weight = 50
    max_value, selected = solve_knapsack(items, max_weight)
    assert max_value == 220
    assert set(selected) == {1, 2}

def test_invalid_items_type():
    """Test with invalid items type"""
    with pytest.raises(ValueError, match="Items must be a list"):
        solve_knapsack("not a list", 10)

def test_invalid_max_weight():
    """Test with invalid max weight"""
    with pytest.raises(ValueError, match="Max weight must be a non-negative number"):
        solve_knapsack([(1, 2), (3, 4)], -5)

def test_invalid_item_structure():
    """Test with invalid item structure"""
    with pytest.raises(ValueError, match="Each item must be a"):
        solve_knapsack([(1, 2), "invalid"], 10)

def test_negative_item_values():
    """Test with negative item weights or values"""
    with pytest.raises(ValueError, match="Item weights and values cannot be negative"):
        solve_knapsack([(1, -2), (3, 4)], 10)

def test_float_weights_and_values():
    """Test with float weights and values"""
    items = [(2.5, 3.0), (3.5, 4.5), (4.0, 5.0)]
    max_weight = 10.0
    max_value, selected = solve_knapsack(items, max_weight)
    assert max_value == 9.5
    assert set(selected) == {0, 1}