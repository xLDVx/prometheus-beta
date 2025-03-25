import pytest
from src.matrix_search import search_matrix

def test_matrix_search_basic():
    matrix = [
        [1, 3, 5, 7],
        [10, 11, 16, 20],
        [23, 30, 34, 60]
    ]
    assert search_matrix(matrix, 3) == True
    assert search_matrix(matrix, 13) == False

def test_matrix_search_edge_cases():
    # Empty matrix
    assert search_matrix([], 5) == False
    assert search_matrix([[], []], 5) == False
    
    # Single row matrix
    matrix_single_row = [[1, 3, 5]]
    assert search_matrix(matrix_single_row, 3) == True
    assert search_matrix(matrix_single_row, 4) == False
    
    # Single column matrix
    matrix_single_col = [[1], [3], [5]]
    assert search_matrix(matrix_single_col, 3) == True
    assert search_matrix(matrix_single_col, 4) == False

def test_matrix_search_boundary_values():
    matrix = [
        [1, 3, 5, 7],
        [10, 11, 16, 20],
        [23, 30, 34, 60]
    ]
    # First and last elements
    assert search_matrix(matrix, 1) == True
    assert search_matrix(matrix, 60) == True
    
    # Values outside the matrix range
    assert search_matrix(matrix, 0) == False
    assert search_matrix(matrix, 61) == False

def test_matrix_search_error_handling():
    # Non-integer target
    with pytest.raises(TypeError, match="Target must be an integer"):
        search_matrix([[1, 2], [3, 4]], "5")
    
    # Non-list matrix
    with pytest.raises(TypeError, match="Matrix must be a list of lists"):
        search_matrix("not a matrix", 5)
    
    # Matrix with non-integer elements
    with pytest.raises(ValueError, match="Matrix must contain only integers"):
        search_matrix([[1, 2], ['a', 4]], 5)

def test_matrix_search_unsorted_rows():
    # Matrix with rows in different orders, but each row sorted
    matrix = [
        [10, 20, 30, 40],
        [15, 25, 35, 45],
        [5, 15, 25, 35]
    ]
    assert search_matrix(matrix, 25) == True
    assert search_matrix(matrix, 26) == False