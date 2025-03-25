from typing import List, Dict, Tuple, Any, Optional
import heapq

class Node:
    """
    Represents a node in the graph with a unique identifier and type.
    
    Attributes:
        id (Any): Unique identifier for the node
        type (str): Type of the node
    """
    def __init__(self, id: Any, type: str):
        self.id = id
        self.type = type
    
    def __eq__(self, other):
        return self.id == other.id and self.type == other.type
    
    def __hash__(self):
        return hash((self.id, self.type))
    
    def __repr__(self):
        return f"Node(id={self.id}, type={self.type})"

def find_shortest_path(nodes: List[Node], edges: List[Tuple[Node, Node, float]]) -> Optional[List[Node]]:
    """
    Find the shortest path between two nodes in a weighted directed graph.
    
    Args:
        nodes (List[Node]): List of nodes in the graph
        edges (List[Tuple[Node, Node, float]]): List of edges with source, destination, and weight
    
    Returns:
        Optional[List[Node]]: Shortest path between source and target nodes, or None if no path exists
    
    Raises:
        ValueError: If nodes list is empty or edges contain invalid nodes
    """
    # Validate input
    if not nodes:
        raise ValueError("Nodes list cannot be empty")
    
    # Create adjacency list representation of the graph
    graph = {}
    for node in nodes:
        graph[node] = []
    
    for source, dest, weight in edges:
        if source not in nodes or dest not in nodes:
            raise ValueError(f"Invalid nodes in edge: {source} -> {dest}")
        graph[source].append((dest, weight))
    
    # Identify source and target nodes (first and last in the nodes list)
    source = nodes[0]
    target = nodes[-1]
    
    # Dijkstra's algorithm
    distances = {node: float('inf') for node in nodes}
    distances[source] = 0
    previous = {node: None for node in nodes}
    
    # Priority queue for efficient path finding
    pq = [(0, source)]
    
    while pq:
        current_distance, current_node = heapq.heappop(pq)
        
        # If we've reached the target, reconstruct and return the path
        if current_node == target:
            path = []
            while current_node:
                path.append(current_node)
                current_node = previous[current_node]
            return list(reversed(path))
        
        # If we've found a longer path, skip
        if current_distance > distances[current_node]:
            continue
        
        # Check neighbors
        for neighbor, weight in graph[current_node]:
            distance = current_distance + weight
            
            # Update if we've found a shorter path
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                previous[neighbor] = current_node
                heapq.heappush(pq, (distance, neighbor))
    
    # No path found
    return None