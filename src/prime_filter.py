def filter_primes(numbers):
    """
    Filter a list of numbers to return only prime numbers.
    
    Args:
        numbers (list): A list of integers to filter.
    
    Returns:
        list: A list of prime numbers from the input list.
    
    Notes:
        - Handles both positive and negative numbers
        - 0 and 1 are not considered prime
        - Negative numbers are not considered prime
    """
    def is_prime(n):
        # Handle non-prime cases first
        if n <= 1:
            return False
        
        # Check for primality using trial division
        for i in range(2, int(abs(n)**0.5) + 1):
            if n % i == 0:
                return False
        
        return True
    
    # Filter and return prime numbers
    return [num for num in numbers if is_prime(num)]