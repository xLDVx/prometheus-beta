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
    # Track seen numbers and their first indices
    first_indices = {}
    # Track which numbers have been seen more than once
    duplicates = set()

    # First pass: track indices and identify duplicates
    for i, num in enumerate(numbers):
        if num in first_indices:
            duplicates.add(num)
        else:
            first_indices[num] = i

    # Second pass: return duplicates in order of first appearance
    result = []
    seen_duplicates = set()
    for num in numbers:
        if num in duplicates and num not in seen_duplicates:
            result.append(num)
            seen_duplicates.add(num)

    return result