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

    # Determine the length of the longer string
    max_length = max(len(input_string1), len(input_string2))

    # Create lists to store the swapped case characters
    swapped_chars = []

    # Iterate through the characters of both strings
    for i in range(max_length):
        # Get characters from both strings, or use empty string if index out of range
        char1 = input_string1[i] if i < len(input_string1) else ''
        char2 = input_string2[i] if i < len(input_string2) else ''

        # Swap the case of characters
        if char1:
            swapped_chars.append(char1.swapcase())
        if char2:
            swapped_chars.append(char2.swapcase())

    # Join the swapped characters into a single string
    return ''.join(swapped_chars)