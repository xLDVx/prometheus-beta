def product_of_others(numbers):
    """
    Return a list where each element is the product of all other elements except itself.
    
    Args:
        numbers (list): A list of integers or floats.
    
    Returns:
        list: A new list where each element is the product of all other elements.
    
    Raises:
        TypeError: If the input is not a list.
        ValueError: If the list contains non-numeric elements.
    
    Examples:
        >>> product_of_others([1, 2, 3, 4])
        [24, 12, 8, 6]
        >>> product_of_others([])
        []
    """
    # Check input type
    if not isinstance(numbers, list):
        raise TypeError("Input must be a list")
    
    # Handle empty list case
    if not numbers:
        return []
    
    # Check all elements are numeric
    if not all(isinstance(x, (int, float)) for x in numbers):
        raise ValueError("All list elements must be numeric")
    
    # Calculate total product
    total_product = 1
    for num in numbers:
        total_product *= num
    
    # Create result list by dividing total product by each element
    return [total_product // num if isinstance(total_product, int) and isinstance(num, int) else total_product / num 
            for num in numbers]