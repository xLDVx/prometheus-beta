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

    # Special case handling for empty strings
    if not input_string1 and not input_string2:
        return ""
    elif not input_string1:
        return input_string2.upper()
    elif not input_string2:
        return input_string1.swapcase()

    # Swap the case of first string, upper/preserve the case of second string
    swapped1 = input_string1.swapcase()
    swapped2 = input_string2.upper()

    return swapped1 + swapped2