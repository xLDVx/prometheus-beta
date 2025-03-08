def count_staircase_ways(stair_lengths):
    """
    Calculate the number of ways to climb a staircase with given step lengths.
    
    Args:
        stair_lengths (list): A list of integers representing the length of each step.
    
    Returns:
        int: The total number of unique ways to climb the staircase.
    
    Raises:
        ValueError: If stair_lengths is None or contains non-positive integers.
    """
    # Validate input
    if stair_lengths is None:
        raise ValueError("Stair lengths cannot be None")
    
    if any(length <= 0 for length in stair_lengths):
        raise ValueError("All stair lengths must be positive integers")
    
    # Total staircase length
    total_length = sum(stair_lengths)
    
    # Dynamic programming to count climbing ways
    # Initialize DP table with base cases
    dp = [0] * (total_length + 1)
    dp[0] = 1  # Base case: one way to climb 0 steps
    
    # Compute ways for each step
    for length in range(1, total_length + 1):
        # Can climb 1 or 2 steps at a time
        if length >= 1:
            dp[length] += dp[length - 1]
        if length >= 2:
            dp[length] += dp[length - 2]
    
    return dp[total_length]