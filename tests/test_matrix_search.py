import pytest
from src.matrix_search import find_matrix_coordinates

def test_find_matrix_coordinates_basic():
    """Test basic matrix search functionality"""
    matrix = [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9]
    ]
    assert find_matrix_coordinates(matrix, 5) == (1, 1)
    assert find_matrix_coordinates(matrix, 9) == (2, 2)
    assert find_matrix_coordinates(matrix, 1) == (0, 0)

def test_find_matrix_coordinates_not_found():
    """Test when target is not in the matrix"""
    matrix = [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9]
    ]
    assert find_matrix_coordinates(matrix, 10) is None

def test_find_matrix_coordinates_first_occurrence():
    """Test that the first occurrence is returned for duplicate values"""
    matrix = [
        [1, 2, 3],
        [2, 2, 6],
        [7, 2, 9]
    ]
    assert find_matrix_coordinates(matrix, 2) == (0, 1)

def test_find_matrix_coordinates_empty_matrix():
    """Test error handling for empty matrix"""
    with pytest.raises(ValueError, match="Matrix must be a non-empty 2D list"):
        find_matrix_coordinates([], 5)
    with pytest.raises(ValueError, match="Matrix must be a non-empty 2D list"):
        find_matrix_coordinates(None, 5)

def test_find_matrix_coordinates_inconsistent_matrix():
    """Test error handling for inconsistent matrix rows"""
    with pytest.raises(ValueError, match="All rows in the matrix must have the same length"):
        find_matrix_coordinates([[1, 2], [3, 4, 5]], 5)

def test_find_matrix_coordinates_different_types():
    """Test searching for different types of values"""
    matrix = [
        [1, 'a', 3],
        ['b', 5, 'c'],
        [7, 8, 9]
    ]
    assert find_matrix_coordinates(matrix, 'a') == (0, 1)
    assert find_matrix_coordinates(matrix, 5) == (1, 1)
    assert find_matrix_coordinates(matrix, 'b') == (1, 0)
    assert find_matrix_coordinates(matrix, 10) is None