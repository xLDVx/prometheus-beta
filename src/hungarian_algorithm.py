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
    
    # Optimization: track best path for each row
    row_cover = [False] * n
    col_cover = [False] * n
    
    # Step 1: Row reduction
    for i in range(n):
        row_min = matrix[i].min()
        matrix[i] -= row_min
    
    # Step 2: Column reduction
    for j in range(n):
        col_min = matrix[:, j].min()
        matrix[:, j] -= col_min
    
    # Find initial assignment
    assignments = [-1] * n
    for i in range(n):
        # Find zero in uncovered row with no other zeros in its column
        zero_cols = np.where(matrix[i] == 0)[0]
        for col in zero_cols:
            if not col_cover[col]:
                assignments[i] = col
                row_cover[i] = True
                col_cover[col] = True
                break
    
    # Find minimum cost assignment
    def find_optimal_assignment():
        max_iterations = n * n  # Prevent infinite loop
        for _ in range(max_iterations):
            # Check if assignment is complete
            if all(x != -1 for x in assignments):
                return assignments
            
            # Find zeros and cover lines
            zero_lines = 0
            # Reset covers
            row_cover[:] = [False] * n
            col_cover[:] = [False] * n
            
            # Cover rows and columns of assigned zeros
            for i in range(n):
                if assignments[i] != -1:
                    row_cover[i] = True
                    col_cover[assignments[i]] = True
            
            # Find the smallest uncovered value
            min_val = float('inf')
            for i in range(n):
                for j in range(n):
                    if not row_cover[i] and not col_cover[j]:
                        min_val = min(min_val, matrix[i, j])
            
            # Adjust matrix
            for i in range(n):
                for j in range(n):
                    # Add min to covered rows
                    if row_cover[i]:
                        matrix[i, j] += min_val
                    # Subtract min from uncovered columns
                    if not col_cover[j]:
                        matrix[i, j] -= min_val
            
            # Try to find new assignments
            for i in range(n):
                if assignments[i] == -1:
                    zero_cols = np.where(matrix[i] == 0)[0]
                    for col in zero_cols:
                        if not col_cover[col]:
                            assignments[i] = col
                            row_cover[i] = True
                            col_cover[col] = True
                            break
        
        return assignments
    
    # Find the optimal assignment
    assignments = find_optimal_assignment()
    
    # Calculate total cost
    total_cost = sum(cost_matrix[i][assignments[i]] for i in range(n))
    
    return total_cost, assignments