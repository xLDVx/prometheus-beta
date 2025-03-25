def bead_sort(arr):
    """
    Implement the bead sort algorithm for positive integers.
    
    Bead sort is a natural sorting algorithm that works by simulating 
    physical beads on parallel rods. It only works with positive integers.
    
    Args:
        arr (list): A list of positive integers to be sorted.
    
    Returns:
        list: A new list with elements sorted in ascending order.
    
    Raises:
        ValueError: If the input contains non-positive integers.
        TypeError: If the input is not a list or contains non-integer elements.
    """
    # Input validation
    if not isinstance(arr, list):
        raise TypeError("Input must be a list")
    
    # Check for non-integer or non-positive elements
    if any(not isinstance(x, int) or x < 0 for x in arr):
        raise ValueError("All elements must be positive integers")
    
    # If list is empty or has only one element, return as is
    if len(arr) <= 1:
        return arr.copy()
    
    # Initialize the sorting space
    max_num = max(arr)
    
    # Create a 2D grid representing the beads
    grid = [[1 if j < num else 0 for j in range(max_num)] for num in arr]
    
    # Simulate gravity by dropping beads
    for col in range(max_num):
        # Count total beads in this column
        col_sum = sum(row[col] for row in grid)
        
        # Drop beads down
        for row in grid:
            row[col] = 1 if col < col_sum else 0
    
    # Reconstruct the sorted array
    sorted_arr = [sum(row) for row in grid]
    
    return sorted_arr