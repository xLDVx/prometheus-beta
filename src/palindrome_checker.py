def is_palindrome(s: str) -> bool:
    """
    Check if a given string is a palindrome.

    A palindrome is a word, phrase, or sequence of characters that reads the same 
    backward as forward. This function is case-insensitive and ignores 
    punctuation, whitespace, and considers both alphabetic and numeric characters.

    Args:
        s (str): The input string to check for palindrome property.

    Returns:
        bool: True if the string is a palindrome, False otherwise.

    Examples:
        >>> is_palindrome("racecar")
        True
        >>> is_palindrome("Was it a car or a cat I saw?")
        True
        >>> is_palindrome("hello")
        False
    """
    # Convert to lowercase and remove non-alphanumeric characters
    cleaned_str = ''.join(char.lower() for char in s if char.isalnum())
    
    # Compare the cleaned string with its reverse
    return cleaned_str == cleaned_str[::-1]