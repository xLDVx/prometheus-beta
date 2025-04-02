def sum_primes_under_n(n):
    """
    Calculate the sum of all prime numbers less than a given positive integer n.
    
    A prime number is a number greater than 1 that is divisible only by 1 and itself.
    
    Args:
        n (int): A positive integer upper bound (exclusive)
    
    Returns:
        int: Sum of all prime numbers less than n
    
    Raises:
        ValueError: If n is not a positive integer
    """
    # Validate input
    if not isinstance(n, int):
        raise ValueError("Input must be an integer")
    if n < 2:
        return 0
    
    # Use Sieve of Eratosthenes to find primes
    # Create a boolean array "is_prime[0..n]" and initialize 
    # all entries it as true. A value in is_prime[i] will 
    # finally be false if i is Not a prime, else true.
    is_prime = [True] * n
    is_prime[0] = is_prime[1] = False
    
    # Use Sieve of Eratosthenes to mark non-primes
    for i in range(2, int(n**0.5) + 1):
        if is_prime[i]:
            # Update all multiples of i starting from i*i
            for j in range(i*i, n, i):
                is_prime[j] = False
    
    # Sum all prime numbers
    return sum(i for i in range(2, n) if is_prime[i])