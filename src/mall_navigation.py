import networkx as nx
from typing import Dict, List, Optional

class MallMap:
    """
    A class representing a mall map as a weighted graph for navigation.
    
    The mall map uses NetworkX to store store connections
    and find the shortest path between two stores.
    """
    
    def __init__(self):
        """
        Initialize an empty mall map using NetworkX graph.
        """
        self._graph = nx.Graph()
    
    def add_connection(self, store1: str, store2: str, distance: float):
        """
        Add a connection between two stores with a given distance.
        
        Args:
            store1 (str): Name of the first store
            store2 (str): Name of the second store
            distance (float): Distance between the stores
        
        Raises:
            ValueError: If either store name is empty or distance is negative
        """
        # Validate inputs
        if not store1 or not store2:
            raise ValueError("Store names cannot be empty")
        if distance < 0:
            raise ValueError("Distance cannot be negative")
        
        # Add the edge to the graph with the distance as weight
        self._graph.add_edge(store1, store2, weight=distance)
    
    def find_shortest_path(self, start: str, end: str) -> Optional[List[str]]:
        """
        Find the shortest path between two stores using NetworkX's shortest path.
        
        Args:
            start (str): Starting store name
            end (str): Destination store name
        
        Returns:
            Optional[List[str]]: List of stores forming the shortest path, 
            or None if no path exists
        
        Raises:
            ValueError: If start store does not exist
        """
        # Check if start store exists
        if start not in self._graph:
            raise ValueError(f"Start store '{start}' does not exist in the mall map")
        
        # Handle different scenarios
        try:
            # If end store is not in graph, raise specific error or return None
            if end not in self._graph:
                return None
            
            # If start and end are the same, return single-store path
            if start == end:
                return [start]
            
            # Find and return the shortest path
            return list(nx.shortest_path(self._graph, start, end))
        
        except nx.NetworkXNoPath:
            # No path exists between stores
            return None