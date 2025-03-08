def find_matrix_coordinates(matrix, target):
    """
    Find the coordinates of a target value in a 2D matrix.
    
    Args:
        matrix (list of lists): A 2D matrix to search through
        target (any): The value to find in the matrix
    
    Returns:
        tuple: A tuple of (row, col) coordinates if found, or None if not found
    
    Raises:
        TypeError: If matrix is not a valid 2D list
        ValueError: If matrix is empty or inconsistent
    """
    # Validate input matrix
    if not matrix or not isinstance(matrix, list):
        raise ValueError("Matrix must be a non-empty 2D list")
    
    # Check matrix consistency
    row_lengths = set(len(row) for row in matrix)
    if len(row_lengths) > 1:
        raise ValueError("All rows in the matrix must have the same length")
    
    # Iterate through matrix to find target
    for row_idx, row in enumerate(matrix):
        for col_idx, value in enumerate(row):
            if value == target:
                return (row_idx, col_idx)
    
    # Target not found
    return None