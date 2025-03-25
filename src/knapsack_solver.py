def solve_knapsack(items, max_weight):
    """
    Solve the 0/1 Knapsack Problem using dynamic programming.
    
    Args:
        items (list): A list of tuples, where each tuple contains (weight, value)
        max_weight (int): Maximum weight capacity of the knapsack
    
    Returns:
        tuple: A tuple containing (max_value, selected_items)
            - max_value (int): Total value of the selected items
            - selected_items (list): List of indices of items selected
    
    Raises:
        ValueError: If inputs are invalid
    """
    # Input validation
    if not isinstance(items, list):
        raise ValueError("Items must be a list of (weight, value) tuples")
    
    if not isinstance(max_weight, (int, float)) or max_weight < 0:
        raise ValueError("Max weight must be a non-negative number")
    
    # Ensure items are valid
    for item in items:
        if not (isinstance(item, (list, tuple)) and len(item) == 2):
            raise ValueError("Each item must be a (weight, value) tuple")
        if not (isinstance(item[0], (int, float)) and isinstance(item[1], (int, float))):
            raise ValueError("Item weights and values must be numbers")
        if item[0] < 0 or item[1] < 0:
            raise ValueError("Item weights and values cannot be negative")
    
    # If no items or zero capacity, return empty result
    if not items or max_weight == 0:
        return 0, []
    
    # Number of items
    n = len(items)
    
    # Convert max_weight to integer to avoid floating-point issues
    max_weight = int(max_weight)
    
    # Create DP table
    dp = [[0 for _ in range(max_weight + 1)] for _ in range(n + 1)]
    
    # Build the DP table
    for i in range(1, n + 1):
        weight, value = items[i-1]
        weight = int(weight)  # Convert to int to handle float weights
        for w in range(max_weight + 1):
            if weight > w:
                # Can't include this item
                dp[i][w] = dp[i-1][w]
            else:
                # Choose max of including or excluding the item
                dp[i][w] = max(
                    dp[i-1][w],  # exclude item
                    dp[i-1][w-weight] + value  # include item
                )
    
    # Backtrack to find selected items
    selected_items = []
    w = max_weight
    
    # Find the combination with the specified value
    for i in range(n, 0, -1):
        if w >= 0 and dp[i][w] != dp[i-1][w]:
            # This item was included
            selected_items.append(i-1)
            w -= int(items[i-1][0])
    
    # Reverse to maintain original order
    selected_items.reverse()
    
    return dp[n][max_weight], selected_items