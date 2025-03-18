def convert_to_inverse_case(input_string):
    """
    Convert a string to inverse case.
    
    In inverse case, uppercase letters become lowercase and 
    lowercase letters become uppercase. Non-alphabetic characters 
    remain unchanged.
    
    Args:
        input_string (str): The string to be converted to inverse case.
    
    Returns:
        str: The string converted to inverse case.
    
    Raises:
        TypeError: If the input is not a string.
    
    Examples:
        >>> convert_to_inverse_case("Hello World!")
        'hELLO wORLD!'
        >>> convert_to_inverse_case("Python 3.9")
        'pYTHON 3.9'
    """
    # Check if input is a string
    if not isinstance(input_string, str):
        raise TypeError("Input must be a string")
    
    # Convert each character to its inverse case
    return ''.join(
        char.lower() if char.isupper() else char.upper() 
        for char in input_string
    )