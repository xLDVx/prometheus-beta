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
    
    # Find the maximum number to determine the number of rods needed
    max_num = max(arr)
    
    # Create the initial bead configuration
    beads = []
    for num in arr:
        # Create beads for each number
        rod = [1] * num
        beads.append(rod)
    
    # Simulate gravity (dropping beads)
    for col in range(max_num):
        # Count beads in each column
        col_count = sum(1 for rod in beads if len(rod) > col)
        
        # Drop beads
        for i in range(len(beads)):
            if len(beads[i]) > col:
                beads[i] = [1] * col_count + [0] * (len(beads[i]) - col_count)
    
    # Reconstruct the sorted array
    sorted_arr = [len(rod) for rod in beads]
    
    return sorted_arr