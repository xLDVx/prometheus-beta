def gcd(a: int, b: int) -> int:
    """
    Calculate the Greatest Common Divisor (GCD) using recursion.
    
    Args:
        a (int): First integer
        b (int): Second integer
    
    Returns:
        int: Greatest Common Divisor of a and b
    
    Raises:
        ValueError: If either input is negative
    """
    # Validate inputs
    if a < 0 or b < 0:
        raise ValueError("Inputs must be non-negative integers")
    
    # Base case: if b is 0, return a
    if b == 0:
        return a
    
    # Recursive case: use Euclidean algorithm
    return gcd(b, a % b)

def lcm(a: int, b: int) -> int:
    """
    Calculate the Least Common Multiple (LCM) using recursion.
    
    Uses the formula: LCM(a,b) = |a * b| / GCD(a,b)
    
    Args:
        a (int): First integer
        b (int): Second integer
    
    Returns:
        int: Least Common Multiple of a and b
    
    Raises:
        ValueError: If either input is negative
        ZeroDivisionError: If both inputs are 0
    """
    # Handle special cases
    if a == 0 and b == 0:
        raise ZeroDivisionError("LCM is undefined when both inputs are 0")
    
    # If either number is 0, return 0
    if a == 0 or b == 0:
        return 0
    
    # Calculate LCM using GCD
    return abs(a * b) // gcd(a, b)