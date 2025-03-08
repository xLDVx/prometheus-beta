def filter_and_sort_odd_integers(numbers):
    """
    Filter and sort odd integers from a given list of integers.

    Args:
        numbers (list): A list of integers to filter and sort.

    Returns:
        list: A new list containing only the odd integers, sorted in ascending order.

    Raises:
        TypeError: If the input is not a list or contains non-integer elements.
    """
    # Validate input is a list
    if not isinstance(numbers, list):
        raise TypeError("Input must be a list")
    
    # Validate all elements are integers
    if not all(isinstance(num, int) for num in numbers):
        raise TypeError("All elements must be integers")
    
    # Filter odd integers and sort them
    odd_integers = sorted([num for num in numbers if num % 2 != 0])
    
    return odd_integers