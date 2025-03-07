def convert_to_uppercase_with_spaces(input_string):
    """
    Convert a string to uppercase, preserving existing spaces and adding spaces between words.

    Args:
        input_string (str): The input string to be converted.

    Returns:
        str: The converted string in uppercase with spaces.

    Raises:
        TypeError: If the input is not a string.
    """
    # Check if input is a string
    if not isinstance(input_string, str):
        raise TypeError("Input must be a string")
    
    # If input is empty, return empty string
    if not input_string:
        return ""
    
    # Convert to uppercase and add spaces between words
    result = []
    for i, char in enumerate(input_string):
        # Add space before uppercase letters (except the first character)
        if i > 0 and char.isupper() and not input_string[i-1].isupper():
            result.append(' ')
        result.append(char.upper())
    
    return ''.join(result)