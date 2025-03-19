from typing import List, Generator

def fibonacci_sequence(n: int) -> List[int]:
    """
    Generate the first n numbers of the Fibonacci sequence.
    
    Args:
        n (int): Number of Fibonacci sequence elements to generate.
    
    Returns:
        List[int]: A list containing the first n Fibonacci numbers.
    
    Raises:
        ValueError: If n is negative.
    
    Time Complexity: O(n)
    Space Complexity: O(n)
    """
    # Validate input
    if not isinstance(n, int):
        raise TypeError("Input must be an integer")
    
    if n < 0:
        raise ValueError("Input must be a non-negative integer")
    
    # Handle edge cases
    if n == 0:
        return []
    if n == 1:
        return [0]
    if n == 2:
        return [0, 1]
    
    # Use generator function with memoization to create Fibonacci sequence
    def fib_generator() -> Generator[int, None, None]:
        # Memoization to store previously calculated Fibonacci numbers
        memo = {0: 0, 1: 1}
        
        def fib(k: int) -> int:
            # Check if already in memo, if not calculate recursively
            if k not in memo:
                memo[k] = fib(k-1) + fib(k-2)
            return memo[k]
        
        # Generate Fibonacci numbers
        for i in range(n):
            yield fib(i)
    
    # Convert generator to list
    return list(fib_generator())