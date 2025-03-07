def kadanes_max_subarray_sum(arr):
    """
    Implement Kadane's algorithm to find the maximum subarray sum.
    
    Args:
        arr (list): A list of integers to find the maximum subarray sum.
    
    Returns:
        int: The maximum sum of any contiguous subarray within the input array.
    
    Raises:
        TypeError: If the input is not a list.
        ValueError: If the list is empty.
    
    Examples:
        >>> kadanes_max_subarray_sum([-2, 1, -3, 4, -1, 2, 1, -5, 4])
        6
        >>> kadanes_max_subarray_sum([1])
        1
        >>> kadanes_max_subarray_sum([-1, -2, -3])
        -1
    """
    # Type and input validation
    if not isinstance(arr, list):
        raise TypeError("Input must be a list of integers")
    
    if not arr:
        raise ValueError("Input list cannot be empty")
    
    # Initialize variables
    max_so_far = current_max = arr[0]
    
    # Iterate through the array starting from the second element
    for num in arr[1:]:
        # Choose between extending the current subarray or starting a new one
        current_max = max(num, current_max + num)
        
        # Update the overall maximum if needed
        max_so_far = max(max_so_far, current_max)
    
    return max_so_far