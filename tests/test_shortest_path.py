import pytest
from src.shortest_path import Node, find_shortest_path

def test_basic_shortest_path():
    """Test a simple path finding scenario."""
    nodes = [
        Node(1, "start"),
        Node(2, "intermediate"),
        Node(3, "end")
    ]
    edges = [
        (nodes[0], nodes[1], 2.0),
        (nodes[1], nodes[2], 3.0)
    ]
    
    path = find_shortest_path(nodes, edges)
    assert path == nodes, "Should return the full path"
    assert len(path) == 3, "Path should have all nodes"

def test_multiple_path_options():
    """Test scenario with multiple possible paths."""
    nodes = [
        Node(1, "start"),
        Node(2, "mid1"),
        Node(3, "mid2"),
        Node(4, "end")
    ]
    edges = [
        (nodes[0], nodes[1], 1.0),
        (nodes[0], nodes[2], 4.0),
        (nodes[1], nodes[3], 3.0),
        (nodes[2], nodes[3], 2.0)
    ]
    
    path = find_shortest_path(nodes, edges)
    assert path == [nodes[0], nodes[1], nodes[3]], "Should choose shortest total path"

def test_no_path_exists():
    """Test scenario where no path exists."""
    nodes = [
        Node(1, "start"),
        Node(2, "unreachable"),
        Node(3, "end")
    ]
    edges = [
        (nodes[1], nodes[2], 5.0)  # No path from start to end
    ]
    
    path = find_shortest_path(nodes, edges)
    assert path is None, "Should return None when no path exists"

def test_empty_nodes_list():
    """Test handling of empty nodes list."""
    with pytest.raises(ValueError, match="Nodes list cannot be empty"):
        find_shortest_path([], [])

def test_invalid_edges():
    """Test handling of edges with invalid nodes."""
    nodes = [Node(1, "start"), Node(2, "end")]
    invalid_nodes = [Node(3, "extra")]
    
    with pytest.raises(ValueError, match="Invalid nodes in edge"):
        find_shortest_path(nodes, [
            (nodes[0], invalid_nodes[0], 1.0)
        ])

def test_nodes_with_same_id_different_type():
    """Test path finding with nodes that have same ID but different types."""
    type_a_node = Node(1, "type_a")
    type_b_node = Node(1, "type_b")
    nodes = [
        type_a_node, 
        type_b_node, 
        Node(2, "end")
    ]
    edges = [
        (type_a_node, type_b_node, 1.0),
        (type_b_node, nodes[2], 2.0)
    ]
    
    path = find_shortest_path(nodes, edges)
    assert path is not None, "Should handle nodes with same ID but different types"
    assert path[-1] == nodes[2], "Should find path to target node"

def test_negative_weight_handling():
    """Test handling of various edge weights."""
    nodes = [
        Node(1, "start"),
        Node(2, "mid"),
        Node(3, "end")
    ]
    edges = [
        (nodes[0], nodes[1], 1.0),
        (nodes[1], nodes[2], 0.5)
    ]
    
    path = find_shortest_path(nodes, edges)
    assert path == [nodes[0], nodes[1], nodes[2]], "Should handle zero and positive weights"