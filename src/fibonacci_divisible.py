def generate_modified_fibonacci(n):
    """
    Generate a modified Fibonacci sequence up to n where the sum of any two consecutive 
    numbers (starting from the third number) is always divisible by 3.

    Args:
        n (int): The upper limit for the Fibonacci sequence values.

    Returns:
        list: A modified Fibonacci sequence meeting the divisibility constraint.

    Raises:
        ValueError: If n is not a positive integer.
    """
    # Validate input
    if not isinstance(n, int) or n < 0:
        raise ValueError("Input must be a non-negative integer")
    
    # Handle edge cases
    if n == 0:
        return []
    if n == 1:
        return [1]
    if n == 2:
        return [1, 1]
    
    # Initialize the sequence
    sequence = [1, 1]
    
    while True:
        # Calculate next number
        next_num = sequence[-1] + sequence[-2]
        
        # If next number exceeds n, stop
        if next_num > n:
            break
        
        # Check divisibility constraint
        if len(sequence) >= 2:
            # From the third number onward, check divisibility
            if (sequence[-1] + sequence[-2]) % 3 != 0:
                # If not divisible, adjust the next number
                while (sequence[-1] + sequence[-2]) % 3 != 0:
                    next_num += 1
        
        sequence.append(next_num)
    
    return sequence