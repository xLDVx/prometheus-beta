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
    # Track seen numbers
    seen = set()
    # Track first duplicate numbers in order
    first_duplicates = []
    # Track logged duplicates to avoid repetition
    logged_duplicates = set()

    for num in numbers:
        # If the number is already seen and not yet logged
        if num in seen and num not in logged_duplicates:
            first_duplicates.append(num)
            logged_duplicates.add(num)
        else:
            # Mark the number as seen
            seen.add(num)

    return first_duplicates