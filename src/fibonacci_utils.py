def fibonacci(n):
    """
    Generate Fibonacci sequence up to a given number.
    
    Args:
        n (int): The maximum number in the Fibonacci sequence.
    
    Returns:
        list: Fibonacci sequence numbers less than or equal to n.
    
    Raises:
        ValueError: If input is not a positive integer.
    """
    if not isinstance(n, int) or n < 0:
        raise ValueError("Input must be a non-negative integer")
    
    # Handle special cases
    if n == 0:
        return []
    if n == 1:
        return [1]
    
    # Generate Fibonacci sequence
    fib_seq = [1, 1]
    while True:
        next_num = fib_seq[-1] + fib_seq[-2]
        if next_num > n:
            break
        fib_seq.append(next_num)
    
    return fib_seq

def fibonacci_sum(numbers):
    """
    Calculate the sum of Fibonacci sequence up to the largest number in the input array.
    
    Args:
        numbers (list): A list of positive integers.
    
    Returns:
        int: Sum of Fibonacci numbers less than or equal to the max input number.
    
    Raises:
        ValueError: If input is not a list of positive integers.
    """
    # Validate input
    if not numbers:
        return 0
    
    if not all(isinstance(x, int) and x > 0 for x in numbers):
        raise ValueError("Input must be a list of positive integers")
    
    # Find the maximum number to generate Fibonacci sequence
    max_num = max(numbers)
    
    # Generate Fibonacci sequence and calculate sum
    fib_seq = fibonacci(max_num)
    return sum(fib_seq)