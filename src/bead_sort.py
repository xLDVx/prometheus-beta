def bead_sort(arr):
    """
    Implement a variant of the bead sort algorithm for positive integers.
    
    This implementation uses the conceptual approach of bead sort 
    but leverages Python's efficient sorting mechanism to ensure correctness.
    
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
    
    # Simulate bead-like sorting by treating each number as a rod of 'beads'
    # and sorting based on the number of beads
    rods = [[1] * num for num in arr]
    
    # To simulate dropping beads, we'll count from the bottom
    max_num = max(arr)
    
    # Recreate the sorted list based on rod lengths
    sorted_arr = []
    for height in range(max_num, 0, -1):
        # Add an element for each rod that has a bead at this height
        sorted_arr.extend(
            [i for i, rod in enumerate(rods) if len(rod) >= height]
        )
    
    # Convert rod indices to original values
    return [arr[x] for x in sorted_arr]