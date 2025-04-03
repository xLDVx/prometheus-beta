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
    
    # Calculate products
    result = []
    for i in range(len(numbers)):
        # Calculate product of all other elements
        product = 1
        for j in range(len(numbers)):
            if i != j:
                product *= numbers[j]
        result.append(product)
    
    return result