import pytest
import math
from src.floyd_warshall import floyd_warshall

def test_simple_graph():
    """Test a simple graph with known shortest paths."""
    graph = [
        [0, 5, float('inf'), 10],
        [float('inf'), 0, 3, float('inf')],
        [float('inf'), float('inf'), 0, 1],
        [float('inf'), float('inf'), float('inf'), 0]
    ]
    expected = [
        [0, 5, 8, 9],
        [float('inf'), 0, 3, 4],
        [float('inf'), float('inf'), 0, 1],
        [float('inf'), float('inf'), float('inf'), 0]
    ]
    result = floyd_warshall(graph)
    assert result == expected

def test_fully_connected_graph():
    """Test a fully connected graph."""
    graph = [
        [0, 1, 4],
        [1, 0, 2],
        [4, 2, 0]
    ]
    expected = [
        [0, 1, 3],
        [1, 0, 2],
        [3, 2, 0]
    ]
    result = floyd_warshall(graph)
    assert result == expected

def test_graph_with_negative_edges():
    """Test a graph with negative edges but no negative cycles."""
    graph = [
        [0, -1, 4],
        [float('inf'), 0, 3],
        [float('inf'), float('inf'), 0]
    ]
    expected = [
        [0, -1, 2],
        [float('inf'), 0, 3],
        [float('inf'), float('inf'), 0]
    ]
    result = floyd_warshall(graph)
    assert result == expected

def test_negative_cycle_detection():
    """Test detection of negative cycles."""
    graph = [
        [0, 1, float('inf')],
        [float('inf'), 0, -3],
        [-1, float('inf'), 0]
    ]
    result = floyd_warshall(graph)
    assert result is None

def test_empty_graph_raises_error():
    """Test that empty graph raises a ValueError."""
    with pytest.raises(ValueError, match="Graph cannot be empty"):
        floyd_warshall([])

def test_non_square_matrix_raises_error():
    """Test that non-square matrix raises a ValueError."""
    with pytest.raises(ValueError, match="Graph must be a square matrix"):
        floyd_warshall([
            [0, 1, 2],
            [3, 4]
        ])

def test_single_vertex_graph():
    """Test a graph with a single vertex."""
    graph = [[0]]
    expected = [[0]]
    result = floyd_warshall(graph)
    assert result == expected