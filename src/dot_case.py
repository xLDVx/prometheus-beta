def convert_to_dot_case(input_string: str) -> str:
    """
    Convert a string to dot case.
    
    Dot case converts a string by replacing spaces, underscores, 
    and camel case separators with dots, and converting to lowercase.
    
    Args:
        input_string (str): The input string to convert.
    
    Returns:
        str: The converted string in dot case.
    
    Raises:
        TypeError: If the input is not a string.
    
    Examples:
        >>> convert_to_dot_case("hello world")
        'hello.world'
        >>> convert_to_dot_case("Hello_World")
        'hello.world'
        >>> convert_to_dot_case("helloWorld")
        'hello.world'
    """
    # Validate input type
    if not isinstance(input_string, str):
        raise TypeError("Input must be a string")
    
    # If input is empty, return empty string
    if not input_string:
        return ""
    
    # Replace non-alphanumeric sequences with dots
    import re
    
    # First, handle camel case by inserting dots before capital letters
    # Use regex to insert a dot before any capital letter that is preceded by a lowercase letter
    camel_case_converted = re.sub(r'([a-z0-9])([A-Z])', r'\1.\2', input_string)
    
    # Convert to lowercase and replace any non-alphanumeric sequences with a single dot
    dot_case = re.sub(r'[^a-z0-9]+', '.', camel_case_converted.lower())
    
    # Remove leading or trailing dots
    dot_case = dot_case.strip('.')
    
    return dot_case