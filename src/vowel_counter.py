def count_vowels_and_consonants(text: str) -> dict:
    """
    Count the number of vowels and consonants in a given string.

    Args:
        text (str): The input string to analyze.

    Returns:
        dict: A dictionary containing the count of vowels and consonants.
              Keys are 'vowels' and 'consonants', with integer values.

    Raises:
        TypeError: If the input is not a string.
    """
    # Validate input
    if not isinstance(text, str):
        raise TypeError("Input must be a string")

    # Convert to lowercase for consistent counting
    text = text.lower()

    # Define vowels (including accented vowels)
    vowels = set('aeiouáéíóúäëïöüâêîôû')

    # Initialize counters
    vowel_count = 0
    consonant_count = 0

    # Count vowels and consonants
    for char in text:
        # Only count alphabetic characters
        if char.isalpha():
            if char in vowels:
                vowel_count += 1
            else:
                consonant_count += 1

    return {
        'vowels': vowel_count,
        'consonants': consonant_count
    }