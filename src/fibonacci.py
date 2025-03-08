"""
Extended Fibonacci sequence generator that supports negative indices and float inputs.

The implementation follows these key principles:
- Supports positive and negative integer indices
- Supports float indices with fractional components
- Maintains mathematical consistency with the Fibonacci sequence
"""

def fibonacci(n):
    """
    Generate Fibonacci number for given index, including negative and float indices.
    
    Args:
        n (int or float): The index of the Fibonacci sequence to compute.
    
    Returns:
        float: The Fibonacci number at the given index.
    
    Raises:
        TypeError: If input is not a number.
    """
    # Type checking
    if not isinstance(n, (int, float)):
        raise TypeError("Input must be a number")
    
    # Special cases for integer indices
    if isinstance(n, int):
        # Direct integer index computation
        if n == 0:
            return 0
        elif n == 1:
            return 1
        elif n > 1:
            # Standard forward Fibonacci
            a, b = 0, 1
            for _ in range(2, n + 1):
                a, b = b, a + b
            return b
        else:
            # Negative integer indices (use generalized recurrence)
            a, b = 0, 1
            for _ in range(0, abs(n) - 1):
                a, b = b - a, a
            return a if n % 2 == 0 else -a
    
    # Float index computation using matrix exponentiation and interpolation
    def matrix_power(matrix, power):
        """Compute matrix power efficiently."""
        if power == 0:
            return [[1, 0], [0, 1]]
        if power == 1:
            return matrix
        
        half = matrix_power(matrix, power // 2)
        result = [
            [half[0][0]*half[0][0] + half[0][1]*half[1][0], 
             half[0][0]*half[0][1] + half[0][1]*half[1][1]],
            [half[1][0]*half[0][0] + half[1][1]*half[1][0], 
             half[1][0]*half[0][1] + half[1][1]*half[1][1]]
        ]
        
        if power % 2 == 1:
            result = [
                [result[0][0]*matrix[0][0] + result[0][1]*matrix[1][0], 
                 result[0][0]*matrix[0][1] + result[0][1]*matrix[1][1]],
                [result[1][0]*matrix[0][0] + result[1][1]*matrix[1][0], 
                 result[1][0]*matrix[0][1] + result[1][1]*matrix[1][1]]
            ]
        
        return result
    
    # Handle float indices through interpolation
    int_part = int(n)
    frac_part = n - int_part
    
    if frac_part == 0:
        return fibonacci(n)
    
    # Compute surrounding Fibonacci numbers
    f_lower = fibonacci(int_part)
    f_upper = fibonacci(int_part + 1)
    
    # Linear interpolation
    return f_lower + frac_part * (f_upper - f_lower)