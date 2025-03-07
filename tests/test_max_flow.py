import pytest
from src.max_flow import ford_fulkerson

def test_basic_max_flow():
    """Test a simple graph with a known maximum flow."""
    graph = {
        's': {'a': 10, 'c': 10},
        'a': {'b': 4, 'c': 2, 'd': 8},
        'b': {'t': 10},
        'c': {'d': 9},
        'd': {'b': 6, 't': 10},
        't': {}
    }
    assert ford_fulkerson(graph, 's', 't') == 19

def test_disconnected_graph():
    """Test a graph with no path from source to sink."""
    graph = {
        's': {},
        'a': {'b': 5},
        'b': {'a': 5},
        't': {}
    }
    assert ford_fulkerson(graph, 's', 't') == 0

def test_single_edge_graph():
    """Test a graph with a single edge."""
    graph = {
        's': {'t': 5},
        't': {}
    }
    assert ford_fulkerson(graph, 's', 't') == 5

def test_complex_graph():
    """Test a more complex graph with multiple paths."""
    graph = {
        's': {'a': 3, 'b': 2, 'c': 3},
        'a': {'b': 1, 'c': 3, 'd': 4},
        'b': {'d': 2, 'e': 2},
        'c': {'e': 1, 'f': 2},
        'd': {'t': 3},
        'e': {'t': 3},
        'f': {'t': 4},
        't': {}
    }
    # Actual maximum flow is 8
    assert ford_fulkerson(graph, 's', 't') == 8

def test_invalid_source_or_sink():
    """Test that an error is raised for invalid source or sink."""
    graph = {
        'a': {'b': 5},
        'b': {'a': 5}
    }
    with pytest.raises(ValueError, match="Source or sink node not found in the graph"):
        ford_fulkerson(graph, 's', 't')

def test_zero_capacity_graph():
    """Test a graph with zero capacities."""
    graph = {
        's': {'a': 0, 'b': 0},
        'a': {'t': 0},
        'b': {'t': 0},
        't': {}
    }
    assert ford_fulkerson(graph, 's', 't') == 0

def test_symmetric_graph():
    """Test a graph with symmetric capacities."""
    graph = {
        's': {'a': 10, 'b': 10},
        'a': {'s': 10, 'b': 2, 't': 4},
        'b': {'s': 10, 'a': 2, 't': 8},
        't': {}
    }
    # Actual maximum flow is 12
    assert ford_fulkerson(graph, 's', 't') == 12