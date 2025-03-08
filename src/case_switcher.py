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

    # Special case handling
    if not input_string1:
        return input_string2.swapcase()  # First string empty
    if not input_string2:
        return input_string1.swapcase()  # Second string empty

    # Swap case of first string, swapcase of second string
    swapped1 = ''.join(c.swapcase() for c in input_string1)
    swapped2 = ''.join(c.swapcase() for c in input_string2)

    return swapped1 + swapped2