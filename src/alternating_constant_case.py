def convert_to_alternating_constant_case(input_string):
    """
    Convert a string to alternating constant case.
    
    This function takes a string and converts it so that:
    - Every even-indexed alphabetic character is converted to UPPERCASE
    - Every odd-indexed alphabetic character is converted to lowercase
    - Skips indexing for non-alphabetic characters
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
    alpha_index = 0
    for char in input_string:
        if char.isalpha():
            # Apply alternating case to alphabetic characters
            if alpha_index % 2 == 0:
                result.append(char.upper())
            else:
                result.append(char.lower())
            alpha_index += 1
        else:
            # Non-alphabetic characters unchanged
            result.append(char)
    
    return ''.join(result)