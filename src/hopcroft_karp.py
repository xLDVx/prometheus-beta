from typing import Dict, List, Optional, Set

class HopcroftKarp:
    """
    Implementation of the Hopcroft-Karp algorithm for maximum matching in bipartite graphs.
    
    The algorithm finds the maximum matching in a bipartite graph efficiently.
    Time complexity: O(E * sqrt(V)), where E is the number of edges and V is the number of vertices.
    """
    
    def __init__(self, graph: Dict[int, List[int]]):
        """
        Initialize the Hopcroft-Karp algorithm with a bipartite graph.
        
        :param graph: A dictionary representing the bipartite graph where keys are vertices 
                      from the left set and values are lists of adjacent vertices from the right set.
        """
        self.graph = graph
        self.match = {}  # Matching dictionary
        self.dist = {}   # Distance dictionary for BFS
    
    def bfs(self) -> bool:
        """
        Breadth-first search to find augmenting paths.
        
        :return: Boolean indicating if an augmenting path exists
        """
        queue = []
        
        # Initialize distances for unmatched vertices in the left set
        for u in self.graph:
            if self.match.get(u) is None:
                self.dist[u] = 0
                queue.append(u)
            else:
                self.dist[u] = float('inf')
        
        # Use sentinel to indicate no augmenting path
        self.dist[None] = float('inf')
        
        while queue:
            u = queue.pop(0)
            
            if self.dist[u] < self.dist[None]:
                for v in self.graph[u]:
                    # Consider unmatched or matched vertices in right set
                    w = self.match.get(v)
                    
                    if self.dist[w] == float('inf'):
                        self.dist[w] = self.dist[u] + 1
                        queue.append(w)
        
        # Return whether an augmenting path exists
        return self.dist[None] != float('inf')
    
    def dfs(self, u: Optional[int]) -> bool:
        """
        Depth-first search to find augmenting paths.
        
        :param u: Vertex to start DFS from
        :return: Boolean indicating if an augmenting path was found
        """
        if u is not None:
            for v in self.graph[u]:
                w = self.match.get(v)
                
                # If no path exists or can extend an existing path
                if (w is None or 
                    (self.dist[w] == self.dist[u] + 1 and self.dfs(w))):
                    self.match[v] = u
                    self.match[u] = v
                    return True
            
            # Mark this vertex as unreachable
            self.dist[u] = float('inf')
            return False
        
        return True
    
    def maximum_matching(self) -> Dict[int, int]:
        """
        Compute the maximum matching in the bipartite graph.
        
        :return: A dictionary representing the maximum matching
        """
        # Reset matching
        self.match.clear()
        
        # While augmenting paths exist, find and use them
        while self.bfs():
            for u in self.graph:
                if self.match.get(u) is None:
                    self.dfs(u)
        
        return self.match