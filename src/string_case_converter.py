def convert_to_alternating_dot_case(input_string):
    """
    Convert a string to alternating dot case.
    
    In alternating dot case, characters alternate between lowercase and uppercase,
    with dots between each character.
    
    Args:
        input_string (str): The input string to be converted.
    
    Returns:
        str: The string converted to alternating dot case.
    
    Raises:
        TypeError: If input is not a string.
        
    Examples:
        >>> convert_to_alternating_dot_case("hello")
        'h.E.l.L.o'
        >>> convert_to_alternating_dot_case("WORLD")
        'w.O.r.L.d'
        >>> convert_to_alternating_dot_case("")
        ''
    """
    # Check if input is a string
    if not isinstance(input_string, str):
        raise TypeError("Input must be a string")
    
    # Handle empty string case
    if not input_string:
        return ""
    
    # Convert to alternating dot case
    result = []
    is_letter_sequence = False
    for i, char in enumerate(input_string):
        # Determine if the current character is a letter
        is_current_letter = char.isalpha()
        
        # Start or continue letter sequence
        if is_current_letter:
            # For letters, apply alternating case
            if not is_letter_sequence or i % 2 == 0:
                char = char.lower()
            else:
                char = char.upper()
            is_letter_sequence = True
        else:
            # Reset letter sequence for non-letter characters
            is_letter_sequence = False
        
        # If not the first character, add a dot
        if i > 0:
            result.append('.')
        
        result.append(char)
    
    return ''.join(result)