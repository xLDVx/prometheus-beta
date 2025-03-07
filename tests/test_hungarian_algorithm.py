import pytest
import numpy as np
from src.hungarian_algorithm import hungarian_algorithm

def test_basic_assignment():
    """Test a simple 3x3 assignment matrix"""
    cost_matrix = [
        [3, 2, 3],
        [1, 5, 4],
        [2, 4, 6]
    ]
    total_cost, assignments = hungarian_algorithm(cost_matrix)
    
    # Verify total cost and assignments
    assert total_cost == 5  # Minimum possible assignment
    assert len(assignments) == 3
    
    # Verify each worker is assigned to a unique job
    assert len(set(assignments)) == 3

def test_rectangular_matrix_error():
    """Test that non-square matrix raises ValueError"""
    with pytest.raises(ValueError):
        hungarian_algorithm([
            [1, 2, 3],
            [4, 5, 6]
        ])

def test_empty_matrix_error():
    """Test that empty matrix raises ValueError"""
    with pytest.raises(ValueError):
        hungarian_algorithm([])

def test_single_element_matrix():
    """Test a 1x1 matrix"""
    cost_matrix = [[5]]
    total_cost, assignments = hungarian_algorithm(cost_matrix)
    
    assert total_cost == 5
    assert assignments == [0]

def test_larger_matrix():
    """Test a larger 4x4 matrix"""
    cost_matrix = [
        [9, 11, 14, 13],
        [12, 13, 16, 15],
        [11, 14, 17, 16],
        [10, 12, 15, 14]
    ]
    total_cost, assignments = hungarian_algorithm(cost_matrix)
    
    # Verify results
    assert total_cost == 46  # Minimum possible assignment
    assert len(assignments) == 4
    assert len(set(assignments)) == 4

def test_matrix_with_zero_values():
    """Test a matrix with zero values"""
    cost_matrix = [
        [0, 2, 3],
        [1, 0, 4],
        [2, 5, 0]
    ]
    total_cost, assignments = hungarian_algorithm(cost_matrix)
    
    # Verify results
    assert total_cost == 0  # Minimum possible assignment
    assert len(assignments) == 3
    assert len(set(assignments)) == 3

def test_equivalent_assignment_options():
    """Test matrix with multiple equivalent assignment options"""
    cost_matrix = [
        [1, 1, 1],
        [1, 1, 1],
        [1, 1, 1]
    ]
    total_cost, assignments = hungarian_algorithm(cost_matrix)
    
    assert total_cost == 3
    assert len(assignments) == 3
    assert len(set(assignments)) == 3