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
    # Track the first occurrence of each duplicate in order
    first_duplicates = []
    # Track seen numbers
    seen = set()
    # Track which duplicates have been logged
    found_duplicates = set()

    # Keep a preserved order of first appearances
    order = []
    for num in numbers:
        # If the number is already seen and not yet logged as a duplicate
        if num in seen and num not in found_duplicates:
            first_duplicates.append(num)
            found_duplicates.add(num)
        else:
            # Mark the number as seen
            seen.add(num)

    return first_duplicates