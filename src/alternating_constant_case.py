def convert_to_alternating_constant_case(input_string):
    """
    Convert a string to alternating constant case.
    
    This function takes a string and converts it so that:
    - Every even-indexed character is converted to UPPERCASE
    - Every odd-indexed character is converted to lowercase
    - Non-alphabetic characters remain unchanged
    
    Args:
        input_string (str): The input string to convert
    
    Returns:
        str: The string converted to alternating constant case
    
    Raises:
        TypeError: If input is not a string
    
    Examples:
        >>> convert_to_alternating_constant_case("hello")
        'HeLlO'
        >>> convert_to_alternating_constant_case("world!")
        'WoRlD!'
    """
    # Check if input is a string
    if not isinstance(input_string, str):
        raise TypeError("Input must be a string")
    
    # If input is empty, return empty string
    if not input_string:
        return ""
    
    # Convert to alternating case
    result = []
    for i, char in enumerate(input_string):
        if i % 2 == 0:
            # Even indices (0, 2, 4...) to UPPERCASE
            result.append(char.upper())
        else:
            # Odd indices (1, 3, 5...) to lowercase
            result.append(char.lower())
    
    return ''.join(result)