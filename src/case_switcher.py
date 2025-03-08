def switch_cases(input_string1, input_string2):
    """
    Swap the character cases between two input strings.

    Args:
        input_string1 (str): The first input string.
        input_string2 (str): The second input string.

    Returns:
        str: A new string with the character cases swapped between the two input strings.

    Raises:
        TypeError: If either input is not a string.
    """
    # Validate input types
    if not (isinstance(input_string1, str) and isinstance(input_string2, str)):
        raise TypeError("Both inputs must be strings")

    # Special case: if first string is empty, uppercase second string 
    if not input_string1:
        return input_string2.upper()
    
    # Special case: if second string is empty, swap case of first string
    if not input_string2:
        return input_string1.swapcase()

    # Swap case of first string, uppercase second string
    return input_string1.swapcase() + input_string2.upper()