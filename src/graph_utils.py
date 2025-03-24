from collections import deque, defaultdict
from typing import Dict, List, Optional

def find_shortest_path(graph: Dict[int, List[int]], start: int, end: int) -> Optional[List[int]]:
    """
    Find the shortest path between start and end nodes in an unweighted graph using BFS.
    
    Args:
        graph (Dict[int, List[int]]): Adjacency list representation of the graph
        start (int): Starting node
        end (int): Target node
    
    Returns:
        Optional[List[int]]: Shortest path from start to end, or None if no path exists
    
    Raises:
        ValueError: If start or end nodes are not in the graph
    """
    # Validate input nodes
    if start not in graph or end not in graph:
        raise ValueError("Start or end node not in graph")
    
    # Handle case where start and end are the same
    if start == end:
        return [start]
    
    # BFS setup
    queue = deque([[start]])
    visited = set([start])
    
    while queue:
        path = queue.popleft()
        node = path[-1]
        
        # Check neighbors
        for neighbor in graph.get(node, []):
            if neighbor == end:
                return path + [neighbor]
            
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append(path + [neighbor])
    
    # No path found
    return None