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
        return [k]

    # Try to generate a sequence with an upper limit to prevent infinite loops
    for start_val in range(1, k * 10):
        sequence = []
        
        # Try to find initial numbers that satisfy the constraint
        for first in range(start_val, start_val + k):
            for second in range(first, first + k):
                if first + second >= k:
                    sequence = [first, second]
                    break
            if sequence:
                break
        
        if not sequence:
            continue

        # Generate the rest of the sequence
        while len(sequence) < n:
            next_num = sequence[-1] + sequence[-2]
            if sequence[-1] + next_num < k:
                break
            sequence.append(next_num)

        # Validate the generated sequence
        if (len(sequence) > 0 and 
            len(sequence) <= n and 
            all(sequence[i] + sequence[i+1] >= k for i in range(len(sequence)-1))):
            return sequence

    # If no valid sequence found
    raise ValueError("Unable to generate a sequence satisfying the constraints")