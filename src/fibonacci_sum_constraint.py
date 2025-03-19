def fibonacci_sum_constraint(n: int, k: int) -> list:
    """
    Generate a Fibonacci-like sequence with specific constraints.

    Args:
        n (int): Maximum length of the sequence
        k (int): Minimum sum of consecutive numbers

    Returns:
        list: A list of numbers forming the constrained Fibonacci sequence

    Raises:
        ValueError: If n or k is not a positive integer or no valid sequence exists
    """
    # Validate input parameters
    if not isinstance(n, int) or n <= 0:
        raise ValueError("n must be a positive integer")
    if not isinstance(k, int) or k < 0:
        raise ValueError("k must be a non-negative integer")

    # Special case: if n is 1, return any valid first number
    if n == 1:
        return [max(1, k)]

    # Absolute maximum value to prevent infinite loops
    MAX_VAL = 10**6

    # Try to generate a sequence with an upper limit to prevent infinite loops
    for start_val in range(1, min(k * 10, MAX_VAL)):
        sequence = []
        
        # Try to find initial numbers that satisfy the constraint
        found_valid_start = False
        for first in range(start_val, min(start_val + k, MAX_VAL)):
            for second in range(first, min(first + k, MAX_VAL)):
                if first + second >= k:
                    sequence = [first, second]
                    found_valid_start = True
                    break
            if found_valid_start:
                break
        
        if not found_valid_start:
            continue

        # Generate the rest of the sequence
        while len(sequence) < n:
            next_num = sequence[-1] + sequence[-2]
            if next_num > MAX_VAL or sequence[-1] + next_num < k:
                break
            sequence.append(next_num)

        # Validate the generated sequence
        if (len(sequence) > 0 and 
            len(sequence) <= n and 
            all(sequence[i] + sequence[i+1] >= k for i in range(len(sequence)-1))):
            return sequence

    # If no valid sequence found
    raise ValueError("Unable to generate a sequence satisfying the constraints")