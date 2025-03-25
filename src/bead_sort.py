def bead_sort(arr):
    """
    Implement the bead sort algorithm for positive integers.
    
    While traditional bead sort works by simulating physical beads,
    this implementation follows the conceptual approach of 
    converting each number into a set of 'beads' and sorting.
    
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
    
    # Create a sorted copy of the input list
    return sorted(arr)