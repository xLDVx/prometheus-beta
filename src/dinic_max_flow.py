from typing import List, Dict
from collections import deque

class DinicMaxFlow:
    """
    Implementation of Dinic's algorithm for maximum flow.
    
    Dinic's algorithm is an efficient algorithm for solving the maximum flow problem
    in a flow network. It uses a combination of breadth-first search and depth-first 
    search to find augmenting paths and maximize flow.
    
    Time Complexity: O(V^2 * E)
    Space Complexity: O(V + E)
    """
    
    def __init__(self, num_vertices: int):
        """
        Initialize the graph for max flow calculation.
        
        Args:
            num_vertices (int): Number of vertices in the graph
        """
        self.num_vertices = num_vertices
        self.graph = [[] for _ in range(num_vertices)]
        self.residual_graph = [[0] * num_vertices for _ in range(num_vertices)]
    
    def add_edge(self, u: int, v: int, capacity: int):
        """
        Add an edge to the graph with a specific capacity.
        
        Args:
            u (int): Source vertex
            v (int): Destination vertex
            capacity (int): Edge capacity
        """
        # Ensure edge is unique and allows multiple edges
        if v not in self.graph[u]:
            self.graph[u].append(v)
            self.graph[v].append(u)
        
        # Add or update edge capacity
        self.residual_graph[u][v] += capacity
    
    def _bfs(self, source: int, sink: int, level: List[int]) -> bool:
        """
        Breadth-first search to create level graph.
        
        Args:
            source (int): Source vertex
            sink (int): Sink vertex
            level (List[int]): Level array to track vertex levels
        
        Returns:
            bool: Whether sink is reachable
        """
        # Reset levels
        level[:] = [-1] * self.num_vertices
        level[source] = 0
        
        queue = deque([source])
        
        while queue:
            u = queue.popleft()
            
            for v in self.graph[u]:
                # If not visited and residual capacity exists
                if level[v] == -1 and self.residual_graph[u][v] > 0:
                    level[v] = level[u] + 1
                    queue.append(v)
        
        return level[sink] != -1
    
    def _dfs(self, u: int, sink: int, flow: int, level: List[int], visited: List[bool]) -> int:
        """
        Depth-first search to find augmenting paths.
        
        Args:
            u (int): Current vertex
            sink (int): Sink vertex
            flow (int): Current possible flow
            level (List[int]): Level of each vertex
            visited (List[bool]): Track visited vertices
        
        Returns:
            int: Augmented flow
        """
        # Reached sink
        if u == sink:
            return flow
        
        visited[u] = True
        
        for v in self.graph[u]:
            if not visited[v] and \
               level[v] == level[u] + 1 and \
               self.residual_graph[u][v] > 0:
                
                curr_flow = min(flow, self.residual_graph[u][v])
                path_flow = self._dfs(v, sink, curr_flow, level, visited)
                
                if path_flow > 0:
                    self.residual_graph[u][v] -= path_flow
                    self.residual_graph[v][u] += path_flow
                    return path_flow
        
        return 0
    
    def max_flow(self, source: int, sink: int) -> int:
        """
        Calculate maximum flow from source to sink.
        
        Args:
            source (int): Source vertex
            sink (int): Sink vertex
        
        Returns:
            int: Maximum flow in the network
        """
        # Validate input
        if source < 0 or source >= self.num_vertices or \
           sink < 0 or sink >= self.num_vertices or \
           source == sink:
            raise ValueError("Invalid source or sink vertex")
        
        # Create copy of original graph
        original_graph = [row[:] for row in self.residual_graph]
        
        max_flow = 0
        level = [-1] * self.num_vertices
        
        # Dinic algorithm core
        while self._bfs(source, sink, level):
            while True:
                visited = [False] * self.num_vertices
                path_flow = self._dfs(source, sink, float('inf'), level, visited)
                
                if path_flow == 0:
                    break
                
                max_flow += path_flow
        
        # Restore original graph
        self.residual_graph = original_graph
        
        return max_flow