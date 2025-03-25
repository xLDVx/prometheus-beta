from typing import List

def find_duplicates(numbers: List[int]) -> List[int]:
    """
    Find and return a list of duplicate integers in the input list.

    Args:
        numbers (List[int]): A list of integers to check for duplicates.

    Returns:
        List[int]: A list of unique integers that appear more than once in the input list.
                   Duplicates are returned only once, preserving their first appearance order.

    Examples:
        >>> find_duplicates([1, 2, 3, 4, 2, 5, 6, 3])
        [2, 3]
        >>> find_duplicates([1, 1, 1, 1])
        [1]
        >>> find_duplicates([])
        []
    """
    # Use sets to track seen and duplicated numbers
    seen = set()
    duplicates = set()
    
    # Use a list to track the order of first duplicate appearances
    result = []

    for num in numbers:
        # If number is already seen and not yet marked as a duplicate
        if num in seen and num not in duplicates:
            # Add the first duplicate appearance in the correct order
            result.append(num)
            duplicates.add(num)
        else:
            # Mark the number as seen
            seen.add(num)

    return result