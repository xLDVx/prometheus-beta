import heapq
from typing import Dict, List, Tuple, Optional

class MallMap:
    """
    A class representing a mall map as a weighted graph for navigation.
    
    The mall map uses an adjacency list representation to store store connections
    and allows finding the shortest path between two stores.
    """
    
    def __init__(self):
        """
        Initialize an empty mall map.
        """
        self.stores = {}
    
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
        
        # Add stores to the graph if not already present
        if store1 not in self.stores:
            self.stores[store1] = {}
        if store2 not in self.stores:
            self.stores[store2] = {}
        
        # Add bidirectional connection
        self.stores[store1][store2] = distance
        self.stores[store2][store1] = distance
    
    def find_shortest_path(self, start: str, end: str) -> Optional[List[str]]:
        """
        Find the shortest path between two stores using Dijkstra's algorithm.
        
        Args:
            start (str): Starting store name
            end (str): Destination store name
        
        Returns:
            Optional[List[str]]: List of stores forming the shortest path, 
            or None if no path exists
        
        Raises:
            ValueError: If start or end store does not exist in the map
        """
        # Validate inputs
        if start not in self.stores:
            raise ValueError(f"Start store '{start}' does not exist in the mall map")
        if end not in self.stores:
            raise ValueError(f"End store '{end}' does not exist in the mall map")
        
        # If start and end are the same, return a path with just that store
        if start == end:
            return [start]
        
        # Initialize Dijkstra's algorithm
        distances = {store: float('inf') for store in self.stores}
        distances[start] = 0
        previous = {store: None for store in self.stores}
        pq = [(0, start)]
        
        # Find shortest path
        while pq:
            current_distance, current_store = heapq.heappop(pq)
            
            # If we've reached the destination, reconstruct and return the path
            if current_store == end:
                path = []
                while current_store:
                    path.append(current_store)
                    current_store = previous[current_store]
                return list(reversed(path))
            
            # If we've found a longer path, skip
            if current_distance > distances[current_store]:
                continue
            
            # Check neighbors
            for neighbor, weight in self.stores[current_store].items():
                distance = current_distance + weight
                
                # If we've found a shorter path, update
                if distance < distances[neighbor]:
                    distances[neighbor] = distance
                    previous[neighbor] = current_store
                    heapq.heappush(pq, (distance, neighbor))
        
        # No path found
        return None