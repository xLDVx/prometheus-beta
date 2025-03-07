from typing import List, Dict
from collections import deque, defaultdict

def ford_fulkerson(graph: Dict[str, Dict[str, int]], source: str, sink: str) -> int:
    """
    Implement the Ford-Fulkerson algorithm to find the maximum flow in a network.
    
    Args:
        graph (Dict[str, Dict[str, int]]): Adjacency list representation of the graph 
            where keys are nodes and values are dictionaries of adjacent nodes and their capacities.
        source (str): The source node from which flow originates.
        sink (str): The sink node where flow terminates.
    
    Returns:
        int: The maximum flow from source to sink.
    
    Raises:
        ValueError: If source or sink nodes are not in the graph.
    """
    # Validate input
    if source not in graph or sink not in graph:
        raise ValueError("Source or sink node not found in the graph")
    
    # Create a deep copy of the graph to avoid modifying the original
    residual_graph = defaultdict(dict)
    for node, edges in graph.items():
        for neighbor, capacity in edges.items():
            residual_graph[node][neighbor] = capacity
            # Ensure backward edges exist for all nodes
            if neighbor not in residual_graph or node not in residual_graph[neighbor]:
                residual_graph[neighbor][node] = 0
    
    def bfs(graph: Dict[str, Dict[str, int]], source: str, sink: str) -> List[str]:
        """Find an augmenting path from source to sink using BFS."""
        # Track visited nodes and their parents
        visited = {node: False for node in graph}
        parent = {node: None for node in graph}
        
        # BFS queue
        queue = deque([source])
        visited[source] = True
        
        while queue:
            current = queue.popleft()
            
            # Check all adjacent nodes
            for neighbor, capacity in graph[current].items():
                if not visited[neighbor] and capacity > 0:
                    queue.append(neighbor)
                    visited[neighbor] = True
                    parent[neighbor] = current
                    
                    # Path found to sink
                    if neighbor == sink:
                        return _reconstruct_path(parent, source, sink)
        
        # No path found
        return []
    
    def _reconstruct_path(parent: Dict[str, str], source: str, sink: str) -> List[str]:
        """Reconstruct the path from source to sink."""
        path = []
        current = sink
        while current is not None:
            path.append(current)
            current = parent[current]
        return list(reversed(path))
    
    def _find_path_flow(graph: Dict[str, Dict[str, int]], path: List[str]) -> int:
        """Find the minimum residual capacity along the path."""
        flow = float('inf')
        for i in range(len(path) - 1):
            current, next_node = path[i], path[i+1]
            flow = min(flow, graph[current][next_node])
        return flow
    
    # Track total maximum flow
    max_flow = 0
    
    # Find augmenting paths
    while True:
        # Find an augmenting path
        path = bfs(residual_graph, source, sink)
        
        # No path found, algorithm terminates
        if not path:
            break
        
        # Find the minimum flow along the path
        path_flow = _find_path_flow(residual_graph, path)
        
        # Update residual graph capacities
        for i in range(len(path) - 1):
            current, next_node = path[i], path[i+1]
            
            # Reduce forward edge capacity
            residual_graph[current][next_node] -= path_flow
            # Add to backward edge
            residual_graph[next_node][current] += path_flow
        
        # Accumulate maximum flow
        max_flow += path_flow
    
    return max_flow