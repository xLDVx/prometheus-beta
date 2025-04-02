import pytest
from src.maze_solver import find_shortest_path, get_neighbors, is_valid

def test_get_neighbors():
    """Test the get_neighbors function returns correct neighboring cells."""
    cell = (2, 3)
    expected_neighbors = [(1, 3), (3, 3), (2, 2), (2, 4)]
    assert sorted(get_neighbors(cell)) == sorted(expected_neighbors)

def test_is_valid_within_bounds():
    """Test is_valid correctly validates cells within maze bounds."""
    maze = [
        [0, 1, 0],
        [2, 0, 3],
        [0, 1, 0]
    ]
    assert is_valid(maze, (0, 0)) == True  # Empty cell
    assert is_valid(maze, (1, 0)) == True  # Start cell
    assert is_valid(maze, (1, 2)) == True  # End cell
    assert is_valid(maze, (0, 1)) == False  # Wall
    assert is_valid(maze, (-1, 0)) == False  # Out of bounds
    assert is_valid(maze, (3, 0)) == False  # Out of bounds

def test_find_shortest_path_simple():
    """Test finding a shortest path in a simple maze."""
    maze = [
        [0, 0, 0],
        [2, 0, 3],
        [0, 0, 0]
    ]
    path = find_shortest_path(maze)
    assert path is not None
    assert len(path) == 3  # Start, one step, end
    assert path[0] == (1, 0)  # Start cell
    assert path[-1] == (1, 2)  # End cell

def test_find_shortest_path_complex():
    """Test finding a shortest path in a more complex maze."""
    maze = [
        [0, 0, 0, 0],
        [2, 1, 0, 3],
        [0, 1, 0, 0],
        [0, 0, 0, 0]
    ]
    path = find_shortest_path(maze)
    assert path is not None
    assert len(path) == 5  # Path around the wall
    assert path[0] == (1, 0)  # Start cell
    assert path[-1] == (1, 3)  # End cell

def test_find_shortest_path_no_path():
    """Test handling of maze with no possible path."""
    maze = [
        [2, 1, 1],
        [1, 1, 1],
        [1, 1, 3]
    ]
    path = find_shortest_path(maze)
    assert path is None

def test_find_shortest_path_invalid_input():
    """Test handling of invalid maze inputs."""
    with pytest.raises(ValueError):
        find_shortest_path([])  # Empty maze
    
    with pytest.raises(ValueError):
        # Maze without start or end
        find_shortest_path([
            [0, 0, 0],
            [0, 0, 0],
            [0, 0, 0]
        ])

def test_find_shortest_path_multiple_start_or_end():
    """Test handling of maze with multiple start or end cells."""
    with pytest.raises(ValueError):
        # Multiple start cells
        find_shortest_path([
            [2, 0, 0],
            [2, 0, 3],
            [0, 0, 0]
        ])