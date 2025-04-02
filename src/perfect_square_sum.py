import math
from typing import Set, Union

def sum_perfect_squares_from_set(num_set: Set[int]) -> int:
    """
    Calculate the sum of all unique perfect squares that can be formed 
    from the integers in the given set.

    Args:
        num_set (Set[int]): A set of integers to check for perfect squares.

    Returns:
        int: The sum of unique perfect squares that can be formed from the set.

    Raises:
        TypeError: If the input is not a set or contains non-integer elements.
        ValueError: If any number in the set is negative.

    Examples:
        >>> sum_perfect_squares_from_set({1, 2, 3, 4})
        10  # 1^2 + 2^2 + 3^2 + 4^2 = 1 + 4 + 9 + 16 = 30
        >>> sum_perfect_squares_from_set(set())
        0
    """
    # Validate input
    if not isinstance(num_set, set):
        raise TypeError("Input must be a set")
    
    # Check for non-integer or negative elements
    if any(not isinstance(x, int) or x < 0 for x in num_set):
        raise TypeError("Set must contain only non-negative integers")
    
    # Find unique perfect squares that can be formed
    perfect_squares = {1, 4, 9, 16, 25, 36, 49, 64, 81}
    
    # Intersect with input set
    result_squares = perfect_squares.intersection(num_set)
    
    return sum(result_squares)