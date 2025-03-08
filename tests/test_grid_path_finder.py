import pytest
from src.grid_path_finder import find_shortest_path

def test_basic_path_exists():
    """Test a simple grid where a path exists"""
    grid = [
        ['.', '.', '.'],
        ['.', 'O', '.'],
        ['.', '.', '.']
    ]
    path = find_shortest_path(grid)
    assert path is not None
    assert len(path) == 5  # Minimum path length
    assert path[0] == (0, 0)
    assert path[-1] == (2, 2)

def test_no_path_blocked_start():
    """Test when start cell is blocked"""
    grid = [
        ['O', '.', '.'],
        ['.', '.', '.'],
        ['.', '.', '.']
    ]
    path = find_shortest_path(grid)
    assert path is None

def test_no_path_blocked_end():
    """Test when end cell is blocked"""
    grid = [
        ['.', '.', '.'],
        ['.', '.', '.'],
        ['.', '.', 'O']
    ]
    path = find_shortest_path(grid)
    assert path is None

def test_complex_path():
    """Test a more complex grid with multiple blocking cells"""
    grid = [
        ['.', '.', '.', '.'],
        ['O', 'O', '.', '.'],
        ['.', '.', 'O', '.'],
        ['.', '.', '.', '.']
    ]
    path = find_shortest_path(grid)
    assert path is not None
    assert len(path) == 7  # Expected path length
    assert path[0] == (0, 0)
    assert path[-1] == (3, 3)

def test_single_cell_grid():
    """Test a single cell grid"""
    grid = [
        ['.']
    ]
    path = find_shortest_path(grid)
    assert path == [(0, 0)]

def test_empty_grid():
    """Test empty grid raises ValueError"""
    with pytest.raises(ValueError):
        find_shortest_path([])

def test_no_possible_path():
    """Test a grid with no possible path"""
    grid = [
        ['.', 'O', '.'],
        ['O', 'O', '.'],
        ['.', '.', '.']
    ]
    path = find_shortest_path(grid)
    assert path is None