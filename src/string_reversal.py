def recursive_reverse_string(s: str) -> str:
    """
    Recursively reverse a string containing lowercase and uppercase letters and spaces.
    
    Args:
        s (str): Input string to be reversed
    
    Returns:
        str: Reversed string
    
    Raises:
        TypeError: If input is not a string
        ValueError: If input contains non-letter and non-space characters
    """
    # Check input type
    if not isinstance(s, str):
        raise TypeError("Input must be a string")
    
    # Check input characters
    if any(not (char.isalpha() or char.isspace()) for char in s):
        raise ValueError("Input can only contain letters and spaces")
    
    # Base case: empty string or single character
    if len(s) <= 1:
        return s
    
    # Recursive case: first character moved to the end, rest of string reversed
    return recursive_reverse_string(s[1:]) + s[0]