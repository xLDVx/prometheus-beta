def fibonacci_sum_constraint(n: int, k: int) -> list:
    """
    Generate a Fibonacci-like sequence with specific constraints.

    Args:
        n (int): Maximum length of the sequence
        k (int): Minimum sum of consecutive numbers

    Returns:
        list: A list of numbers forming the constrained Fibonacci sequence

    Raises:
        ValueError: If n or k is not a positive integer
    """
    # Validate input parameters
    if not isinstance(n, int) or n <= 0:
        raise ValueError("n must be a positive integer")
    if not isinstance(k, int) or k < 0:
        raise ValueError("k must be a non-negative integer")

    # Special case: if n is 1, return any valid first number
    if n == 1:
        return [k]

    # Initialize the sequence
    sequence = []

    # Start with the first two numbers that satisfy the constraint
    for first in range(k, k * 2):
        for second in range(first, k * 2):
            if first + second >= k:
                sequence = [first, second]
                break
        if sequence:
            break

    # If no initial sequence found, raise an error
    if not sequence:
        raise ValueError("Unable to generate a sequence satisfying the constraints")

    # Generate the rest of the sequence
    while len(sequence) < n:
        next_num = sequence[-1] + sequence[-2]
        if sequence[-1] + next_num < k:
            break
        sequence.append(next_num)

    return sequence