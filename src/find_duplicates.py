from typing import List

def find_duplicates(numbers: List[int]) -> List[int]:
    """
    Find and return a list of duplicate integers in the input list.

    Args:
        numbers (List[int]): A list of integers to check for duplicates.

    Returns:
        List[int]: A list of integers that appear more than once in the input list.
                   Duplicates are returned only once, in the order of their first appearance.

    Examples:
        >>> find_duplicates([1, 2, 3, 4, 2, 5, 6, 3])
        [2, 3]
        >>> find_duplicates([1, 1, 1, 1])
        [1]
        >>> find_duplicates([])
        []
    """
    # Use a set to track seen numbers and another to track duplicates
    seen = set()
    duplicates = set()

    for num in numbers:
        # If the number is already in seen, it's a duplicate
        if num in seen:
            duplicates.add(num)
        else:
            seen.add(num)

    # Convert duplicates to a list, preserving the order of first appearance
    return [num for num in numbers if num in duplicates]