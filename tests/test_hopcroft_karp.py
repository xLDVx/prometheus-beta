import pytest
from src.hopcroft_karp import HopcroftKarp

def test_empty_graph():
    """Test maximum matching for an empty graph."""
    graph = {}
    hk = HopcroftKarp(graph)
    assert hk.maximum_matching() == {}

def test_single_edge_graph():
    """Test maximum matching for a graph with a single edge."""
    graph = {
        1: [2]
    }
    hk = HopcroftKarp(graph)
    matching = hk.maximum_matching()
    assert matching == {1: 2, 2: 1}

def test_multiple_edges_graph():
    """Test maximum matching for a graph with multiple possible matches."""
    graph = {
        1: [2, 3],
        2: [1, 4],
        3: [1, 4],
        4: [2, 3]
    }
    hk = HopcroftKarp(graph)
    matching = hk.maximum_matching()
    
    # Validate the maximum matching (each vertex is matched only once)
    matched_left = set()
    matched_right = set()
    for u, v in matching.items():
        if u in graph:  # Left side vertices
            assert v in graph[u]
            assert u not in matched_left
            assert v not in matched_right
            matched_left.add(u)
            matched_right.add(v)

def test_disconnected_graph():
    """Test maximum matching for a disconnected graph."""
    graph = {
        1: [2],
        3: [4],
        5: []
    }
    hk = HopcroftKarp(graph)
    matching = hk.maximum_matching()
    
    assert matching == {1: 2, 2: 1, 3: 4, 4: 3}

def test_no_perfect_matching():
    """Test graph where not all vertices can be matched."""
    graph = {
        1: [2],
        2: [1],
        3: []
    }
    hk = HopcroftKarp(graph)
    matching = hk.maximum_matching()
    
    # Validate that the maximum matching is correct
    assert len(matching) == 2  # 1-2 match, 3 remains unmatched
    assert matching.get(1) == 2
    assert matching.get(2) == 1

def test_large_graph():
    """Test maximum matching for a larger graph."""
    graph = {
        1: [2, 3, 4],
        2: [1, 5],
        3: [1, 5, 6],
        4: [1, 6],
        5: [2, 3],
        6: [3, 4]
    }
    hk = HopcroftKarp(graph)
    matching = hk.maximum_matching()
    
    # Validate the maximum matching
    matched_left = set()
    matched_right = set()
    for u, v in matching.items():
        if u in graph:  # Left side vertices
            assert v in graph[u]
            assert u not in matched_left
            assert v not in matched_right
            matched_left.add(u)
            matched_right.add(v)

def test_invalid_graph_input():
    """Test error handling for invalid graph input."""
    with pytest.raises(TypeError):
        HopcroftKarp(None)
    
    with pytest.raises(TypeError):
        HopcroftKarp([1, 2, 3])