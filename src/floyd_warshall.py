from typing import List, Union, Optional
import math

def floyd_warshall(graph: List[List[Union[int, float]]]) -> Optional[List[List[Union[int, float]]]]:
    """
    Implement the Floyd-Warshall algorithm to find shortest paths between all pairs of vertices.
    
    Args:
        graph (List[List[Union[int, float]]]): An adjacency matrix representing the graph.
                                               Use float('inf') for non-existent edges.
    
    Returns:
        Optional[List[List[Union[int, float]]]]: Distance matrix with shortest paths between all vertices,
                                                 or None if negative cycle is detected.
    
    Raises:
        ValueError: If input graph is not a valid square matrix.
    """
    # Input validation
    if not graph or len(graph) == 0:
        raise ValueError("Graph cannot be empty")
    
    # Check if graph is a square matrix
    n = len(graph)
    if any(len(row) != n for row in graph):
        raise ValueError("Graph must be a square matrix")
    
    # Create a copy of the input graph to avoid modifying the original
    dist = [row.copy() for row in graph]
    
    # Floyd-Warshall algorithm
    for k in range(n):
        # Intermediate vertex
        for i in range(n):
            for j in range(n):
                # Check if path through k is shorter
                if (dist[i][k] != float('inf') and 
                    dist[k][j] != float('inf') and 
                    dist[i][k] + dist[k][j] < dist[i][j]):
                    dist[i][j] = dist[i][k] + dist[k][j]
    
    # Detect negative cycles
    for i in range(n):
        if dist[i][i] < 0:
            return None
    
    return dist