def to_alternating_case(text: str) -> str:
    """
    Convert a string to alternating case (AkA AlTeRnAtInG cAsE).
    
    Args:
        text (str): The input string to be converted.
    
    Returns:
        str: A new string with alternating character cases.
    
    Raises:
        TypeError: If the input is not a string.
    
    Examples:
        >>> to_alternating_case("hello")
        'HeLlO'
        >>> to_alternating_case("WORLD")
        'WoRlD'
        >>> to_alternating_case("")
        ''
    """
    # Check if input is a string
    if not isinstance(text, str):
        raise TypeError("Input must be a string")
    
    # If empty string, return as is
    if not text:
        return text
    
    # Convert to alternating case
    return ''.join(
        char.upper() if i % 2 == 0 else char.lower() 
        for i, char in enumerate(text)
    )