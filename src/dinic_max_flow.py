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
        self.capacity = [[0] * num_vertices for _ in range(num_vertices)]
    
    def add_edge(self, u: int, v: int, capacity: int):
        """
        Add an edge to the graph with a specific capacity.
        
        Args:
            u (int): Source vertex
            v (int): Destination vertex
            capacity (int): Edge capacity
        """
        # Check if edge already exists
        self.graph[u].append(v)
        self.graph[v].append(u)
        self.capacity[u][v] += capacity
    
    def _bfs(self, source: int, sink: int) -> List[int]:
        """
        Breadth-first search to create level graph.
        
        Args:
            source (int): Source vertex
            sink (int): Sink vertex
        
        Returns:
            List[int]: Level of each vertex
        """
        # Reset levels
        level = [-1] * self.num_vertices
        level[source] = 0
        
        queue = deque([source])
        
        while queue:
            u = queue.popleft()
            
            for v in self.graph[u]:
                # If not visited and residual capacity exists
                if level[v] == -1 and self.capacity[u][v] > 0:
                    level[v] = level[u] + 1
                    queue.append(v)
        
        return level
    
    def _dfs(self, u: int, sink: int, flow: int, level: List[int], 
             flow_so_far: int) -> int:
        """
        Depth-first search to find augmenting paths.
        
        Args:
            u (int): Current vertex
            sink (int): Sink vertex
            flow (int): Current possible flow
            level (List[int]): Level of each vertex
            flow_so_far (int): Flow accumulated so far
        
        Returns:
            int: Augmented flow
        """
        # Reached sink, return flow
        if u == sink:
            return flow
        
        for v in self.graph[u]:
            # Check if this path has residual capacity and is a valid level path
            if (level[v] == level[u] + 1 and 
                self.capacity[u][v] > 0):
                
                curr_flow = min(flow, self.capacity[u][v])
                path_flow = self._dfs(v, sink, curr_flow, level, flow_so_far + curr_flow)
                
                if path_flow > 0:
                    self.capacity[u][v] -= path_flow
                    self.capacity[v][u] += path_flow
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
        
        max_flow = 0
        
        # Keep finding augmenting paths
        while True:
            level = self._bfs(source, sink)
            
            # If no path exists, we're done
            if level[sink] == -1:
                break
            
            # Keep finding paths until no more augmenting paths
            while True:
                path_flow = self._dfs(source, sink, float('inf'), level, 0)
                
                if path_flow == 0:
                    break
                
                max_flow += path_flow
        
        return max_flow