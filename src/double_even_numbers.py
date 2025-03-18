def double_even_numbers(numbers):
    """
    Take an array of numbers and return a new array with even numbers multiplied by 2.
    
    Args:
        numbers (list): A list of integers to process
    
    Returns:
        list: A new list with even numbers doubled, odd numbers unchanged
    
    Raises:
        TypeError: If input is not a list or contains non-numeric elements
    """
    # Validate input is a list
    if not isinstance(numbers, list):
        raise TypeError("Input must be a list")
    
    # Validate all elements are numeric
    if not all(isinstance(num, (int, float)) for num in numbers):
        raise TypeError("All elements must be numbers")
    
    # Create new list with even numbers doubled
    return [num * 2 if num % 2 == 0 else num for num in numbers]