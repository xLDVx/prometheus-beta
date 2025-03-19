from typing import List
from collections import deque

def find_shortest_path(grid: List[List[int]]) -> int:
    """
    Find the shortest path in a 2D grid maze from top-left to bottom-right.
    
    Args:
        grid (List[List[int]]): A 2D grid where 0 represents open paths and 1 represents walls.
                                Grid is NxN square.
    
    Returns:
        int: Length of the shortest path, or -1 if no path exists.
    
    Raises:
        ValueError: If the grid is empty or not a square grid.
    """
    # Validate input
    if not grid or not grid[0]:
        raise ValueError("Grid cannot be empty")
    
    # Check if grid is square
    n = len(grid)
    if any(len(row) != n for row in grid):
        raise ValueError("Grid must be a square NxN matrix")
    
    # Possible movement directions: right, down, left, up
    directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
    
    # Create a queue for BFS and a visited set
    queue = deque([(0, 0, 0)])  # (row, col, path_length)
    visited = set([(0, 0)])
    
    # Perform Breadth-First Search
    while queue:
        row, col, path_length = queue.popleft()
        
        # Reached bottom-right corner
        if row == n - 1 and col == n - 1:
            return path_length
        
        # Try all four directions
        for dx, dy in directions:
            new_row, new_col = row + dx, col + dy
            
            # Check if new position is valid
            if (0 <= new_row < n and 
                0 <= new_col < n and 
                grid[new_row][new_col] == 0 and 
                (new_row, new_col) not in visited):
                
                queue.append((new_row, new_col, path_length + 1))
                visited.add((new_row, new_col))
    
    # No path found
    return -1