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
    matrix = np.array(cost_matrix, dtype=float)
    
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
    
    # Track covered rows and columns
    covered_rows = set()
    covered_cols = set()
    
    # Find initial zero assignments
    assignments = [-1] * n
    for i in range(n):
        zero_cols = np.where(matrix[i] == 0)[0]
        for col in zero_cols:
            if col not in covered_cols:
                assignments[i] = col
                covered_rows.add(i)
                covered_cols.add(col)
                break
    
    # Continue until we have a complete assignment
    while len(covered_rows) < n:
        # Find uncovered zeros
        uncovered_zeros = []
        for i in range(n):
            if i not in covered_rows:
                zero_cols = np.where(matrix[i] == 0)[0]
                for col in zero_cols:
                    if col not in covered_cols:
                        uncovered_zeros.append((i, col))
        
        # If no uncovered zeros, modify matrix
        if not uncovered_zeros:
            # Find minimum uncovered value
            min_val = float('inf')
            for i in range(n):
                for j in range(n):
                    if i not in covered_rows and j not in covered_cols:
                        min_val = min(min_val, matrix[i, j])
            
            # Adjust matrix
            for i in range(n):
                for j in range(n):
                    if i in covered_rows:
                        matrix[i, j] += min_val
                    if j not in covered_cols:
                        matrix[i, j] -= min_val
        
        # Assign new zeros
        for i, col in uncovered_zeros:
            if assignments[i] == -1:
                assignments[i] = col
                covered_rows.add(i)
                covered_cols.add(col)
    
    # Calculate total cost
    total_cost = sum(cost_matrix[i][assignments[i]] for i in range(n))
    
    return total_cost, assignments