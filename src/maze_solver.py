from typing import List, Tuple, Optional
from collections import deque

def find_shortest_path(maze: List[List[int]]) -> Optional[List[Tuple[int, int]]]:
    """
    Find the shortest path from the start cell to the end cell in a maze.
    
    Args:
        maze (List[List[int]]): A 2D grid representing the maze
            0: Empty cell
            1: Wall
            2: Start cell
            3: End cell
    
    Returns:
        Optional[List[Tuple[int, int]]]: Shortest path from start to end, 
        or None if no path exists
    
    Raises:
        ValueError: If maze is empty or invalid
    """
    # Validate input
    if not maze or not maze[0]:
        raise ValueError("Maze cannot be empty")
    
    # Find start and end cells
    start = None
    end = None
    for r, row in enumerate(maze):
        for c, cell in enumerate(row):
            if cell == 2:
                start = (r, c)
            elif cell == 3:
                end = (r, c)
    
    # Validate start and end exist
    if start is None or end is None:
        raise ValueError("Maze must contain exactly one start (2) and one end (3) cell")
    
    # BFS to find shortest path
    queue = deque([(start, [start])])
    visited = set([start])
    
    while queue:
        current, path = queue.popleft()
        
        # Check if reached end
        if current == end:
            return path
        
        # Explore neighbors
        neighbors = get_neighbors(current)
        for neighbor in neighbors:
            # Check if neighbor is valid and not visited
            if is_valid(maze, neighbor) and neighbor not in visited:
                visited.add(neighbor)
                queue.append((neighbor, path + [neighbor]))
    
    # No path found
    return None

def get_neighbors(cell: Tuple[int, int]) -> List[Tuple[int, int]]:
    """
    Get potential neighboring cells (up, down, left, right).
    
    Args:
        cell (Tuple[int, int]): Current cell coordinates (row, col)
    
    Returns:
        List[Tuple[int, int]]: List of potential neighboring cell coordinates
    """
    r, c = cell
    return [
        (r-1, c),  # Up
        (r+1, c),  # Down
        (r, c-1),  # Left
        (r, c+1)   # Right
    ]

def is_valid(maze: List[List[int]], cell: Tuple[int, int]) -> bool:
    """
    Check if a cell is within maze boundaries and is an empty cell.
    
    Args:
        maze (List[List[int]]): The maze grid
        cell (Tuple[int, int]): Cell coordinates to check
    
    Returns:
        bool: True if cell is valid (within bounds and empty/start/end), False otherwise
    """
    r, c = cell
    
    # Check boundary conditions
    if (r < 0 or r >= len(maze) or 
        c < 0 or c >= len(maze[0])):
        return False
    
    # Check cell type (0: empty, 2: start, 3: end are valid)
    return maze[r][c] in {0, 2, 3}