def calculate_factorial(n):
    """
    Calculate the factorial of a given non-negative integer.

    Args:
        n (int): A non-negative integer for which factorial will be calculated.

    Returns:
        int: The factorial of the input number.

    Raises:
        ValueError: If the input is a negative number.
        TypeError: If the input is not an integer.
    """
    # Check if input is an integer
    if not isinstance(n, int):
        raise TypeError("Input must be an integer")
    
    # Check if input is non-negative
    if n < 0:
        raise ValueError("Factorial is not defined for negative numbers")
    
    # Handle special cases
    if n == 0 or n == 1:
        return 1
    
    # Calculate factorial using iterative approach
    result = 1
    for i in range(2, n + 1):
        result *= i
    
    return result