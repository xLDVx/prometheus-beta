def find_gcd(a: int, b: int) -> int:
    """
    Find the Greatest Common Divisor (GCD) of two numbers using the Euclidean algorithm.
    
    Args:
        a (int): First integer number
        b (int): Second integer number
    
    Returns:
        int: The greatest common divisor of a and b
    
    Raises:
        TypeError: If inputs are not integers
        ValueError: If inputs are negative
    """
    # Check input types
    if not (isinstance(a, int) and isinstance(b, int)):
        raise TypeError("Inputs must be integers")
    
    # Check for negative inputs
    if a < 0 or b < 0:
        raise ValueError("Inputs must be non-negative integers")
    
    # Handle special cases
    if a == 0:
        return b
    if b == 0:
        return a
    
    # Euclidean algorithm
    while b:
        a, b = b, a % b
    
    return a