def find_missing_numbers(arr):
    """
    Find all missing numbers in a sorted array of positive integers.
    
    Args:
        arr (list): A sorted list of positive integers (ascending or descending).
    
    Returns:
        list: A list of missing numbers between the minimum and maximum values.
    
    Raises:
        ValueError: If the input is not a list of positive integers.
    """
    # Validate input
    if not arr or not all(isinstance(x, int) and x > 0 for x in arr):
        raise ValueError("Input must be a non-empty list of positive integers")
    
    # Determine sorting direction
    is_ascending = arr[0] <= arr[-1]
    
    # If descending, work with the sorted ascending version
    if not is_ascending:
        sorted_arr = sorted(arr)
    else:
        sorted_arr = arr
    
    # Create a set of the input array for efficient lookup
    num_set = set(sorted_arr)
    
    # Determine min and max
    min_val = 1
    max_val = sorted_arr[-1]
    
    # Find missing numbers
    missing = [
        num for num in range(min_val, max_val + 1) 
        if num not in num_set
    ]
    
    # Return in original order
    return sorted(missing, reverse=not is_ascending)