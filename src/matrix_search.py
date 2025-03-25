def search_matrix(matrix, target):
    """
    Search for a target integer in a 2D matrix with sorted inner lists.
    
    Args:
        matrix (List[List[int]]): A 2D matrix where inner lists are sorted 
                                  in ascending order. Rows may not be sorted.
        target (int): The integer to search for in the matrix.
    
    Returns:
        bool: True if the target is found, False otherwise.
    
    Time Complexity: O(m * log n), where m is the number of rows and n is the length of each row
    Space Complexity: O(1)
    
    Raises:
        TypeError: If matrix is not a list of lists or target is not an integer.
        ValueError: If matrix is empty or contains non-integer elements.
    """
    # Input validation
    if not matrix or not isinstance(matrix, list):
        return False
    
    if not all(isinstance(row, list) for row in matrix):
        raise TypeError("Matrix must be a list of lists")
    
    if not isinstance(target, int):
        raise TypeError("Target must be an integer")
    
    # Check if matrix is empty
    if len(matrix) == 0 or len(matrix[0]) == 0:
        return False
    
    # Validate matrix contents
    for row in matrix:
        if not all(isinstance(x, int) for x in row):
            raise ValueError("Matrix must contain only integers")
    
    # Binary search for each row
    for row in matrix:
        # Skip rows where target is out of range
        if not row or target < row[0] or target > row[-1]:
            continue
        
        # Perform binary search on the row
        left, right = 0, len(row) - 1
        while left <= right:
            mid = (left + right) // 2
            if row[mid] == target:
                return True
            elif row[mid] < target:
                left = mid + 1
            else:
                right = mid - 1
    
    return False