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
    
    # Normalize to ascending order for consistent processing
    if not is_ascending:
        arr = sorted(arr, reverse=True)
    
    # Find the range of numbers
    min_val = 1
    max_val = arr[-1]
    
    # If only one element, generate missing numbers before it
    if len(arr) == 1:
        missing = list(range(1, arr[0]))
    else:
        # Create a set of the input array for efficient lookup
        num_set = set(arr)
        
        # Find missing numbers
        missing = [
            num for num in range(min_val, max_val + 1) 
            if num not in num_set
        ]
    
    # If originally descending, return in descending order
    return sorted(missing, reverse=not is_ascending)