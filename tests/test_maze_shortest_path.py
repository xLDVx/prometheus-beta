import pytest
from src.maze_shortest_path import find_shortest_path

def test_simple_path():
    """Test a simple maze with a clear path"""
    maze = [
        [0, 0, 0],
        [0, 0, 0],
        [0, 0, 0]
    ]
    assert find_shortest_path(maze) == 4  # Minimum steps to bottom-right

def test_blocked_start():
    """Test when start is blocked"""
    maze = [
        [1, 0, 0],
        [0, 0, 0],
        [0, 0, 0]
    ]
    assert find_shortest_path(maze) == -1

def test_blocked_end():
    """Test when end is blocked"""
    maze = [
        [0, 0, 0],
        [0, 0, 0],
        [0, 0, 1]
    ]
    assert find_shortest_path(maze) == -1

def test_maze_with_wall_obstacles():
    """Test a maze with wall obstacles"""
    maze = [
        [0, 0, 0],
        [1, 1, 0],
        [0, 0, 0]
    ]
    assert find_shortest_path(maze) == 4

def test_diagonal_movement():
    """Test diagonal movement is allowed"""
    maze = [
        [0, 1, 0],
        [1, 0, 1],
        [0, 1, 0]
    ]
    assert find_shortest_path(maze) == 3

def test_no_path():
    """Test a maze with no possible path"""
    maze = [
        [0, 1, 0],
        [1, 1, 1],
        [0, 1, 0]
    ]
    assert find_shortest_path(maze) == -1

def test_single_cell_maze():
    """Test a single-cell maze"""
    maze = [[0]]
    assert find_shortest_path(maze) == 1

def test_empty_maze():
    """Test empty maze raises ValueError"""
    with pytest.raises(ValueError):
        find_shortest_path([])

def test_irregular_maze():
    """Test maze with irregular row lengths"""
    maze = [
        [0, 0],
        [0, 0, 0],
        [0, 0]
    ]
    assert find_shortest_path(maze) == 4