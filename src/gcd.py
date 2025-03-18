def recursive_gcd(a: int, b: int) -> int:
    """
    Calculate the Greatest Common Divisor (GCD) of two integers using recursion.
    
    This implementation uses the Euclidean algorithm recursively.
    
    Args:
        a (int): First non-negative integer
        b (int): Second non-negative integer
    
    Returns:
        int: The greatest common divisor of a and b
    
    Raises:
        ValueError: If either input is negative
        TypeError: If inputs are not integers
    
    Examples:
        >>> recursive_gcd(48, 18)
        6
        >>> recursive_gcd(54, 24)
        6
        >>> recursive_gcd(0, 5)
        5
        >>> recursive_gcd(5, 0)
        5
    """
    # Type checking
    if not isinstance(a, int) or not isinstance(b, int):
        raise TypeError("Inputs must be integers")
    
    # Negative input validation 
    if a < 0 or b < 0:
        raise ValueError("Inputs must be non-negative integers")
    
    # Base cases
    if b == 0:
        return a
    if a == 0:
        return b
    
    # Recursive case using Euclidean algorithm
    return recursive_gcd(b, a % b)