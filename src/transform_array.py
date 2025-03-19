def transform_array(numbers):
    """
    Transform an array of non-negative integers based on specific rules.
    
    Rules:
    - 0 remains 0
    - Non-zero elements are transformed to their square plus 1
    
    Args:
        numbers (list): A list of non-negative integers
    
    Returns:
        list: A new list with transformed elements
    
    Raises:
        TypeError: If input is not a list
        ValueError: If any element is a negative number
    """
    # Validate input is a list
    if not isinstance(numbers, list):
        raise TypeError("Input must be a list")
    
    # Validate all elements are non-negative integers
    if any(not isinstance(num, int) or num < 0 for num in numbers):
        raise ValueError("All elements must be non-negative integers")
    
    # Transform the array
    return [0 if num == 0 else num**2 + 1 for num in numbers]