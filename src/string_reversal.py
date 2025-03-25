def reverse_string(input_string: str) -> str:
    """
    Reverse the order of characters in the input string.

    Args:
        input_string (str): The string to be reversed.

    Returns:
        str: The input string with characters in reverse order.

    Raises:
        TypeError: If the input is not a string.
    """
    # Check if input is a string
    if not isinstance(input_string, str):
        raise TypeError("Input must be a string")
    
    # Reverse the string using slicing
    return input_string[::-1]