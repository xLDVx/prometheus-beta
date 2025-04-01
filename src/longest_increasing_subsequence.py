def find_longest_increasing_subsequence(arr):
    """
    Find the longest increasing subsequence in the given array.
    
    Args:
        arr (list): Input list of comparable elements
    
    Returns:
        list: The longest increasing subsequence
    
    Raises:
        TypeError: If input is not a list
        ValueError: If input list contains non-comparable elements
    """
    # Validate input
    if not isinstance(arr, list):
        raise TypeError("Input must be a list")
    
    # Handle empty list case
    if not arr:
        return []
    
    # Validate list contains comparable elements
    try:
        _ = all(x <= x for x in arr)
    except TypeError:
        raise ValueError("List contains non-comparable elements")
    
    # Dynamic programming solution to find longest increasing subsequence
    n = len(arr)
    # dp will store the length of LIS ending at each index
    dp = [1] * n
    # prev will help reconstruct the actual subsequence
    prev = [None] * n
    
    # Find the longest increasing subsequence
    max_length = 1
    max_index = 0
    
    for i in range(1, n):
        for j in range(i):
            # Use <= to allow only strictly increasing subsequence
            if arr[i] > arr[j] and dp[i] < dp[j] + 1:
                dp[i] = dp[j] + 1
                prev[i] = j
        
        # Track the overall maximum
        if dp[i] > max_length:
            max_length = dp[i]
            max_index = i
    
    # Reconstruct the subsequence
    subsequence = []
    while max_index is not None:
        subsequence.insert(0, arr[max_index])
        max_index = prev[max_index]
    
    return subsequence