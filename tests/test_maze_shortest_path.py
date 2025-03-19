import pytest
from src.maze_shortest_path import find_shortest_path

def test_basic_path():
    grid = [
        [0, 0, 0],
        [0, 0, 0],
        [0, 0, 0]
    ]
    assert find_shortest_path(grid) == 4  # Path from (0,0) to (2,2)

def test_path_with_walls():
    grid = [
        [0, 0, 0],
        [1, 1, 0],
        [0, 0, 0]
    ]
    assert find_shortest_path(grid) == 4

def test_no_path():
    grid = [
        [0, 1, 0],
        [1, 1, 0],
        [0, 1, 0]
    ]
    assert find_shortest_path(grid) == -1

def test_single_cell():
    grid = [[0]]
    assert find_shortest_path(grid) == 0

def test_start_or_end_blocked():
    grid = [
        [1, 0, 0],
        [0, 0, 0],
        [0, 0, 0]
    ]
    assert find_shortest_path(grid) == -1

def test_larger_grid():
    grid = [
        [0, 0, 0, 0],
        [1, 1, 0, 1],
        [0, 0, 0, 0],
        [0, 1, 1, 0]
    ]
    assert find_shortest_path(grid) == 6

def test_empty_grid_raises_error():
    with pytest.raises(ValueError):
        find_shortest_path([])

def test_non_square_grid_raises_error():
    with pytest.raises(ValueError):
        find_shortest_path([
            [0, 0, 0],
            [0, 0]
        ])