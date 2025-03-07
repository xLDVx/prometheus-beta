import re

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
    
    # Use regex to add spaces before uppercase letters
    # Special handling for consecutive uppercase letters
    spaced_string = re.sub(r'([a-z0-9])([A-Z])', r'\1 \2', input_string)
    
    # Additional regex to handle consecutive uppercase letters
    spaced_string = re.sub(r'([A-Z])([A-Z][a-z])', r'\1 \2', spaced_string)
    
    # Convert to uppercase
    return spaced_string.upper()