def sort_numbers_with_even_squares(numbers):
    """
    Sort an array of numbers with a special sorting rule:
    1. First, sort the entire array in ascending order
    2. Then, replace even numbers with their squares 
    3. Sort the even number squares in descending order
    
    Args:
        numbers (list): A list of numbers to be sorted
    
    Returns:
        list: Sorted list with even numbers squared and sorted
    
    Raises:
        TypeError: If input is not a list
        ValueError: If list contains non-numeric elements
    """
    # Validate input
    if not isinstance(numbers, list):
        raise TypeError("Input must be a list")
    
    # Ensure all elements are numbers
    try:
        numbers = [float(num) for num in numbers]
    except (TypeError, ValueError):
        raise ValueError("All list elements must be numeric")
    
    # Sort the entire list in ascending order
    sorted_nums = sorted(numbers)
    
    # Create a new list to modify
    result = sorted_nums.copy()
    
    # Square even numbers
    for i in range(len(result)):
        if result[i] % 2 == 0:
            result[i] = result[i] ** 2
    
    # Sort the squares of even numbers in descending order
    even_square_indices = [i for i in range(len(result)) if result[i] % 2 == 0]
    
    # Extract even squares, sort them, and put them back
    if even_square_indices:
        even_squares = [result[i] for i in even_square_indices]
        even_squares.sort(reverse=True)
        
        for i, idx in enumerate(even_square_indices):
            result[idx] = even_squares[i]
    
    return result