def sum_unique_even_integers(numbers):
    """
    Calculate the sum of unique even integers in the input array.

    Args:
        numbers (list): A list of integers to process.

    Returns:
        int: Sum of even integers that appear only once in the input list.

    Raises:
        TypeError: If the input is not a list or contains non-integer elements.
    """
    # Validate input
    if not isinstance(numbers, list):
        raise TypeError("Input must be a list")
    
    # Validate list contains only integers
    if not all(isinstance(num, int) for num in numbers):
        raise TypeError("All elements must be integers")
    
    # Count occurrences of even numbers
    even_counts = {}
    for num in numbers:
        if num % 2 == 0:
            even_counts[num] = even_counts.get(num, 0) + 1
    
    # Find unique or largest unique even number
    if any(count > 1 for count in even_counts.values()):
        unique_evens = [num for num, count in even_counts.items() if count == 1]
        return max(unique_evens) if unique_evens else 0
    
    # Sum unique even numbers (those that appear only once)
    unique_even_sum = sum(num for num, count in even_counts.items() if count == 1)
    
    return unique_even_sum