def filter_even_numbers(numbers):
    """
    Filter even numbers from the input list with linear time complexity.
    
    Args:
        numbers (list): A list of integers to filter.
    
    Returns:
        list: A new list containing only the even numbers from the input list.
    
    Raises:
        TypeError: If the input is not a list or contains non-integer elements.
    """
    # Input validation
    if not isinstance(numbers, list):
        raise TypeError("Input must be a list")
    
    # Create a new list to store even numbers
    even_numbers = []
    
    # Iterate through the input list once (linear time complexity)
    for num in numbers:
        # Validate each element is an integer
        if not isinstance(num, int):
            raise TypeError("All list elements must be integers")
        
        # Check if the number is even using modulo operation
        if num % 2 == 0:
            even_numbers.append(num)
    
    return even_numbers