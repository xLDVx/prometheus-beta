def find_min_max_difference(number_string):
    """
    Calculate the difference between the largest and smallest numbers in a comma-separated string of integers.

    Args:
        number_string (str): A string of comma-separated integers.

    Returns:
        int: The difference between the largest and smallest numbers.

    Raises:
        ValueError: If the input string is empty or contains no valid numbers.
    """
    # Check for empty or whitespace-only input
    if not number_string or number_string.isspace():
        raise ValueError("Input string cannot be empty")
    
    try:
        # Split the string and convert to integers, filtering out empty strings
        numbers = [int(num.strip()) for num in number_string.split(',') if num.strip()]
        
        # Check if the list is empty after processing
        if not numbers:
            raise ValueError("No valid numbers found in the input string")
        
        # Find and return the difference between max and min
        return max(numbers) - min(numbers)
    
    except ValueError as e:
        # Catch conversion errors or empty list
        raise ValueError(f"Invalid input: {str(e)}")