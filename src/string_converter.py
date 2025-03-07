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
    
    # If string is already in uppercase with spaces, return as-is
    if input_string.isupper() and ' ' in input_string:
        return input_string
    
    # Convert to uppercase and add spaces between words
    result = []
    prev_was_upper = False
    for i, char in enumerate(input_string):
        # Preserve existing spaces
        if char.isspace():
            result.append(char.upper())
            prev_was_upper = False
            continue
        
        # Add space before uppercase letters
        if i > 0 and char.isupper():
            # Add space if previous char was lowercase 
            # or if this is start of a new uppercase sequence after a lowercase letter
            if not prev_was_upper and not input_string[i-1].isspace():
                result.append(' ')
        
        result.append(char.upper())
        prev_was_upper = char.isupper()
    
    return ''.join(result)