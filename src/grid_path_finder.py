from typing import List, Tuple, Optional
from collections import deque

def find_shortest_path(grid: List[List[str]]) -> Optional[List[Tuple[int, int]]]:
    """
    Find the shortest path from top-left to bottom-right corner of a grid.
    
    Args:
        grid (List[List[str]]): A 2D grid where:
            '.' represents an empty cell
            'O' represents a blocking cell
            '#' represents part of the path
    
    Returns:
        Optional[List[Tuple[int, int]]]: List of coordinates representing the shortest path,
        or None if no path exists.
    
    Raises:
        ValueError: If the grid is empty or invalid
    """
    # Input validation
    if not grid or not grid[0]:
        raise ValueError("Grid cannot be empty")
    
    rows, cols = len(grid), len(grid[0])
    
    # Boundary check and start/end cell validation
    if grid[0][0] == 'O' or grid[rows-1][cols-1] == 'O':
        return None
    
    # Possible movement directions: right, down, left, up
    directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
    
    # Initialize visited set and queue for BFS
    visited = set()
    queue = deque([(0, 0, [(0, 0)])])
    
    while queue:
        x, y, path = queue.popleft()
        
        # Reached bottom-right corner
        if x == rows - 1 and y == cols - 1:
            return path
        
        # Explore adjacent cells
        for dx, dy in directions:
            nx, ny = x + dx, y + dy
            
            # Check if new cell is within grid, not visited, and not blocked
            if (0 <= nx < rows and 
                0 <= ny < cols and 
                grid[nx][ny] != 'O' and 
                (nx, ny) not in visited):
                
                visited.add((nx, ny))
                new_path = path + [(nx, ny)]
                queue.append((nx, ny, new_path))
    
    # No path found
    return None