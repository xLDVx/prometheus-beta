def find_longest_common_suffix(strings):
    """
    Find the longest common suffix among a list of strings.

    Args:
        strings (list): A list of strings to compare.

    Returns:
        str: The longest common suffix. Returns an empty string if 
             no common suffix exists or the input list is empty.

    Raises:
        TypeError: If the input is not a list or contains non-string elements.
    """
    # Check for invalid input
    if not isinstance(strings, list):
        raise TypeError("Input must be a list of strings")
    
    # Handle empty list case
    if not strings:
        return ""
    
    # Check that all elements are strings
    if not all(isinstance(s, str) for s in strings):
        raise TypeError("All elements must be strings")
    
    # Handle case with single string
    if len(strings) == 1:
        return strings[0]
    
    # Find the shortest string to limit suffix length
    shortest = min(strings, key=len)
    
    # Start from the longest possible suffix and work down
    for length in range(len(shortest), 0, -1):
        # Get the potential suffix
        potential_suffix = shortest[-length:]
        
        # Check if this suffix is common to all strings
        if all(s.endswith(potential_suffix) for s in strings):
            return potential_suffix
    
    # If no common suffix found
    return ""