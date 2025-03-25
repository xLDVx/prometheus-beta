def swap_case(input_string):
    """
    Swap the case of characters in the input string.
    
    This function takes a single string input and returns a new string where:
    - Lowercase characters are converted to uppercase
    - Uppercase characters are converted to lowercase
    
    Args:
        input_string (str): The input string to transform
    
    Returns:
        str: A new string with character cases swapped
    
    Examples:
        >>> swap_case('Hello World!')
        'hELLO wORLD!'
        >>> swap_case('PyThOn')
        'pYtHoN'
        >>> swap_case('')
        ''
    """
    # Use the built-in swapcase() method for efficient case swapping
    return input_string.swapcase()