import pytest
from src.graph_utils import find_shortest_path

def test_basic_shortest_path():
    graph = {
        1: [2, 3],
        2: [1, 4],
        3: [1, 4],
        4: [2, 3, 5],
        5: [4]
    }
    path = find_shortest_path(graph, 1, 5)
    assert path == [1, 2, 4, 5] or path == [1, 3, 4, 5]

def test_same_start_and_end():
    graph = {
        1: [2, 3],
        2: [1],
        3: [1]
    }
    path = find_shortest_path(graph, 1, 1)
    assert path == [1]

def test_no_path_exists():
    graph = {
        1: [2],
        2: [1],
        3: [4],
        4: [3]
    }
    path = find_shortest_path(graph, 1, 4)
    assert path is None

def test_invalid_start_node():
    graph = {
        1: [2],
        2: [1]
    }
    with pytest.raises(ValueError):
        find_shortest_path(graph, 3, 1)

def test_invalid_end_node():
    graph = {
        1: [2],
        2: [1]
    }
    with pytest.raises(ValueError):
        find_shortest_path(graph, 1, 3)

def test_complex_graph():
    graph = {
        1: [2, 3],
        2: [1, 4, 5],
        3: [1, 6],
        4: [2],
        5: [2, 6],
        6: [3, 5]
    }
    path = find_shortest_path(graph, 1, 6)
    assert path in [[1, 3, 6], [1, 2, 5, 6]]

def test_disconnected_graph():
    graph = {
        1: [2],
        2: [1],
        3: [4],
        4: [3]
    }
    path = find_shortest_path(graph, 1, 4)
    assert path is None