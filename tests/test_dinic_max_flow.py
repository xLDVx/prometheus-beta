import pytest
import sys
import os

# Add src directory to path
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from src.dinic_max_flow import DinicMaxFlow

def test_basic_max_flow():
    """
    Test a simple max flow scenario
    """
    dinic = DinicMaxFlow(4)
    dinic.add_edge(0, 1, 10)
    dinic.add_edge(0, 2, 10)
    dinic.add_edge(1, 3, 4)
    dinic.add_edge(2, 3, 8)
    
    max_flow = dinic.max_flow(0, 3)
    assert max_flow == 12, f"Expected max flow of 12, got {max_flow}"

def test_disconnected_graph():
    """
    Test max flow in a graph where no path exists from source to sink
    """
    dinic = DinicMaxFlow(3)
    dinic.add_edge(0, 1, 5)
    
    max_flow = dinic.max_flow(0, 2)
    assert max_flow == 0, f"Expected max flow of 0, got {max_flow}"

def test_complex_flow_network():
    """
    Test a more complex flow network
    
    Network structure:
    0 --> 1 (10)
    0 --> 2 (10)
    1 --> 3 (4)
    1 --> 4 (8)
    2 --> 4 (9)
    3 --> 5 (10)
    4 --> 5 (10)
    
    Manually calculated max flow: 14
    """
    dinic = DinicMaxFlow(6)
    dinic.add_edge(0, 1, 10)
    dinic.add_edge(0, 2, 10)
    dinic.add_edge(1, 3, 4)
    dinic.add_edge(1, 4, 8)
    dinic.add_edge(2, 4, 9)
    dinic.add_edge(3, 5, 10)
    dinic.add_edge(4, 5, 10)
    
    max_flow = dinic.max_flow(0, 5)
    print(f"Actual max flow: {max_flow}")
    assert max_flow == 14, f"Expected max flow of 14, got {max_flow}"

def test_invalid_source_sink():
    """
    Test error handling for invalid source or sink vertices
    """
    dinic = DinicMaxFlow(3)
    
    with pytest.raises(ValueError, match="Invalid source or sink vertex"):
        dinic.max_flow(-1, 2)
    
    with pytest.raises(ValueError, match="Invalid source or sink vertex"):
        dinic.max_flow(0, 3)
    
    with pytest.raises(ValueError, match="Invalid source or sink vertex"):
        dinic.max_flow(2, 2)

def test_zero_capacity_edges():
    """
    Test flow network with zero-capacity edges
    """
    dinic = DinicMaxFlow(3)
    dinic.add_edge(0, 1, 0)
    dinic.add_edge(1, 2, 0)
    
    max_flow = dinic.max_flow(0, 2)
    assert max_flow == 0, f"Expected max flow of 0, got {max_flow}"