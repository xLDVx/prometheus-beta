def fibonacci(n):
    """
    Calculate the n-th Fibonacci number using matrix exponentiation with O(log n) time complexity.
    
    Args:
        n (int): The index of the Fibonacci number to calculate (0-based index).
    
    Returns:
        int: The n-th Fibonacci number.
    
    Raises:
        ValueError: If n is negative.
    """
    # Handle edge cases
    if not isinstance(n, int):
        raise TypeError("Input must be an integer")
    
    if n < 0:
        raise ValueError("Input must be a non-negative integer")
    
    # Special cases for first few Fibonacci numbers
    if n <= 1:
        return n
    
    # Matrix exponentiation for O(log n) calculation
    def matrix_multiply(a, b):
        """Multiply two 2x2 matrices."""
        return [
            [a[0][0]*b[0][0] + a[0][1]*b[1][0], a[0][0]*b[0][1] + a[0][1]*b[1][1]],
            [a[1][0]*b[0][0] + a[1][1]*b[1][0], a[1][0]*b[0][1] + a[1][1]*b[1][1]]
        ]
    
    def matrix_power(matrix, power):
        """Calculate matrix to the power using exponentiation by squaring."""
        # Base case
        if power == 0:
            return [[1, 0], [0, 1]]  # Identity matrix
        
        if power == 1:
            return matrix
        
        # Recursively compute matrix power
        half_power = matrix_power(matrix, power // 2)
        result = matrix_multiply(half_power, half_power)
        
        # If power is odd, multiply by original matrix
        if power % 2 == 1:
            result = matrix_multiply(result, matrix)
        
        return result
    
    # Base matrix for Fibonacci calculation
    base_matrix = [[1, 1], [1, 0]]
    
    # Calculate the matrix power and extract the result
    result_matrix = matrix_power(base_matrix, n - 1)
    return result_matrix[0][0]