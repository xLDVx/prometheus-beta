def is_palindrome(input_string: str) -> bool:
    """
    Check if the given string is a palindrome.
    
    A palindrome reads the same backward as forward, considering all characters.
    The function is case-sensitive and preserves special characters and numbers.
    
    Args:
        input_string (str): The string to check for palindrome property
    
    Returns:
        bool: True if the string is a palindrome, False otherwise
    
    Examples:
        >>> is_palindrome("racecar")
        True
        >>> is_palindrome("Hello")
        False
        >>> is_palindrome("A man, a plan, a canal: Panama")
        False
        >>> is_palindrome("12321")
        True
    """
    # If input is not a string, raise a TypeError
    if not isinstance(input_string, str):
        raise TypeError("Input must be a string")
    
    # If string is empty or has only one character, it's a palindrome
    if len(input_string) <= 1:
        return True
    
    # Compare the string with its reverse
    return input_string == input_string[::-1]