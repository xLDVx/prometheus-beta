def remove_duplicate_words(text: str) -> str:
    """
    Remove duplicate words from a given string while preserving the original word order.

    Args:
        text (str): The input string containing words to be deduplicated.

    Returns:
        str: A new string with duplicate words removed, maintaining the first occurrence order.

    Examples:
        >>> remove_duplicate_words("hello hello world")
        'hello world'
        >>> remove_duplicate_words("the quick brown fox jumps the quick brown fox")
        'the quick brown fox jumps'
    """
    # Handle edge cases
    if not isinstance(text, str):
        raise TypeError("Input must be a string")
    
    if not text:
        return ""
    
    # Split the string into words and create a list to track unique words
    words = text.split()
    unique_words = []
    seen = set()
    
    # Iterate through words, keeping only the first occurrence
    for word in words:
        if word not in seen:
            unique_words.append(word)
            seen.add(word)
    
    # Join the unique words back into a string
    return ' '.join(unique_words)