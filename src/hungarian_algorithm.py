import numpy as np

def hungarian_algorithm(cost_matrix):
    """
    Implement the Hungarian algorithm for solving the assignment problem.
    
    The Hungarian algorithm finds the optimal assignment that minimizes the total cost.
    
    Args:
        cost_matrix (list of lists or numpy.ndarray): A square matrix representing 
                    the cost of assigning each worker to each job.
    
    Returns:
        tuple: A tuple containing:
            - The optimal total cost
            - A list of assignments where each index represents a worker 
              and the value represents the assigned job
    
    Raises:
        ValueError: If the input is not a valid square matrix
    """
    # Convert to numpy array for easier manipulation
    matrix = np.array(cost_matrix, dtype=float).copy()
    
    # Validate input
    if matrix.ndim != 2 or matrix.shape[0] != matrix.shape[1]:
        raise ValueError("Input must be a square matrix")
    
    n = matrix.shape[0]
    
    # Step 1: Subtract row minimums
    for i in range(n):
        matrix[i] -= matrix[i].min()
    
    # Step 2: Subtract column minimums
    for j in range(n):
        matrix[:, j] -= matrix[:, j].min()
    
    # Initialize assignments and marks
    row_cover = [False] * n
    col_cover = [False] * n
    starred_zeros = [None] * n
    primed_zeros = [None] * n
    
    # Find initial assignment
    for i in range(n):
        for j in range(n):
            if matrix[i, j] == 0 and not row_cover[i] and not col_cover[j]:
                starred_zeros[i] = j
                row_cover[i] = True
                col_cover[j] = True
                break
    
    # Additional steps for finding optimal assignment
    while True:
        # Find an uncovered zero
        uncovered_zero = None
        for i in range(n):
            if not row_cover[i]:
                for j in range(n):
                    if matrix[i, j] == 0 and not col_cover[j]:
                        uncovered_zero = (i, j)
                        break
                if uncovered_zero:
                    break
        
        # If no uncovered zero, create more
        if uncovered_zero is None:
            # Find minimum uncovered value
            min_val = float('inf')
            for i in range(n):
                for j in range(n):
                    if not row_cover[i] and not col_cover[j]:
                        min_val = min(min_val, matrix[i, j])
            
            # Adjust matrix
            for i in range(n):
                for j in range(n):
                    if row_cover[i]:
                        matrix[i, j] += min_val
                    if not col_cover[j]:
                        matrix[i, j] -= min_val
            
            continue
        
        # Check if zero can be added to assignment
        i, j = uncovered_zero
        if starred_zeros[i] is None:
            # Augmenting path algorithm
            path = []
            path.append((i, j))
            
            while True:
                # Find starred zero in the same column
                starred_row = None
                for r in range(n):
                    if starred_zeros[r] == j:
                        starred_row = r
                        break
                
                if starred_row is None:
                    break
                
                # Find prime zero in the starred zero's row
                primed_col = None
                for c in range(n):
                    if primed_zeros[starred_row] == c:
                        primed_col = c
                        break
                
                path.append((starred_row, j))
                path.append((starred_row, primed_col))
                j = primed_col
                
                # Update starred and primed zeros
                for p_i, p_j in path:
                    if starred_zeros[p_i] == p_j:
                        starred_zeros[p_i] = None
                    if primed_zeros[p_i] == p_j:
                        starred_zeros[p_i] = p_j
                
                # Reset covers and primed zeros
                row_cover = [False] * n
                col_cover = [False] * n
                primed_zeros = [None] * n
                
                # New assignment
                break
    
    # Compute optimal assignment
    assignments = [None] * n
    for i in range(n):
        if starred_zeros[i] is not None:
            assignments[i] = starred_zeros[i]
    
    # Calculate total cost
    total_cost = sum(cost_matrix[i][assignments[i]] for i in range(n))
    
    return total_cost, assignments