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
        self.flows = [[0] * num_vertices for _ in range(num_vertices)]
    
    def add_edge(self, u: int, v: int, capacity: int):
        """
        Add an edge to the graph with a specific capacity.
        
        Args:
            u (int): Source vertex
            v (int): Destination vertex
            capacity (int): Edge capacity
        """
        # Add forward and backward edges
        self.graph[u].append((v, capacity))
        self.graph[v].append((u, 0))  # Residual graph backward edge
    
    def _bfs(self, source: int, sink: int, level: List[int]) -> bool:
        """
        Breadth-first search to create level graph.
        
        Args:
            source (int): Source vertex
            sink (int): Sink vertex
            level (List[int]): Level of each vertex
        
        Returns:
            bool: Whether sink is reachable
        """
        # Reset levels
        level[:] = [-1] * self.num_vertices
        level[source] = 0
        
        queue = deque([source])
        
        while queue:
            u = queue.popleft()
            
            for v, capacity in self.graph[u]:
                # If not visited and residual capacity exists
                if level[v] == -1 and self.flows[u][v] < capacity:
                    level[v] = level[u] + 1
                    queue.append(v)
        
        return level[sink] != -1
    
    def _dfs(self, u: int, sink: int, flow: int, level: List[int], 
             blocked_flow: List[int]) -> int:
        """
        Depth-first search to find augmenting paths.
        
        Args:
            u (int): Current vertex
            sink (int): Sink vertex
            flow (int): Current flow
            level (List[int]): Level of each vertex
            blocked_flow (List[int]): Blocked flow for each vertex
        
        Returns:
            int: Augmented flow
        """
        # Reached sink, return flow
        if u == sink:
            return flow
        
        for i, (v, capacity) in enumerate(self.graph[u]):
            residual_capacity = capacity - self.flows[u][v]
            
            # Check if edge can be used
            if (level[v] == level[u] + 1 and 
                residual_capacity > 0 and 
                blocked_flow[v] == 0):
                
                curr_flow = min(flow, residual_capacity)
                temp_flow = self._dfs(v, sink, curr_flow, level, blocked_flow)
                
                if temp_flow > 0:
                    self.flows[u][v] += temp_flow
                    self.flows[v][u] -= temp_flow
                    return temp_flow
        
        blocked_flow[u] = 1
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
        
        # Reset flows
        self.flows = [[0] * self.num_vertices for _ in range(self.num_vertices)]
        
        total_flow = 0
        level = [-1] * self.num_vertices
        
        # Keep finding augmenting paths
        while self._bfs(source, sink, level):
            while True:
                blocked_flow = [0] * self.num_vertices
                path_flow = self._dfs(source, sink, float('inf'), level, blocked_flow)
                
                if path_flow == 0:
                    break
                
                total_flow += path_flow
        
        return total_flow