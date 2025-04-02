def to_sponge_case(text: str) -> str:
    """
    Convert a string to alternating sponge case (MiXeD cAsE).
    
    Args:
        text (str): The input string to convert.
    
    Returns:
        str: The input string converted to alternating case.
    
    Raises:
        TypeError: If the input is not a string.
    
    Examples:
        >>> to_sponge_case("hello")
        'HeLlO'
        >>> to_sponge_case("WORLD")
        'WoRlD'
        >>> to_sponge_case("")
        ''
    """
    # Check input type
    if not isinstance(text, str):
        raise TypeError("Input must be a string")
    
    # Convert to sponge case
    return ''.join(
        char.upper() if idx % 2 == 0 else char.lower() 
        for idx, char in enumerate(text)
    )