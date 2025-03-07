def symmetric_difference(list1: list, list2: list) -> list:
    """
    Find the symmetric difference between two lists.
    
    The symmetric difference is a list of elements that are in either of the input lists,
    but not in their intersection. This means elements unique to both lists.
    
    Args:
        list1 (list): The first input list
        list2 (list): The second input list
    
    Returns:
        list: A list containing elements unique to both input lists
    
    Example:
        >>> symmetric_difference([1, 2, 3], [3, 4, 5])
        [1, 2, 4, 5]
    """
    # Convert lists to sets for efficient symmetric difference calculation
    set1 = set(list1)
    set2 = set(list2)
    
    # Use symmetric_difference method and convert back to list
    return list(set1.symmetric_difference(set2))