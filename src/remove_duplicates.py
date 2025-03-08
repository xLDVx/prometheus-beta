def remove_duplicates(arr):
    """
    Remove duplicate elements from an array while maintaining O(n) time complexity.
    
    Args:
        arr (list): Input list that may contain duplicate elements
    
    Returns:
        list: A new list with duplicates removed, preserving the original order of first occurrence
    
    Raises:
        TypeError: If input is not a list
    
    Time Complexity: O(n)
    Space Complexity: O(n)
    
    Examples:
        >>> remove_duplicates([1, 2, 3, 2, 4, 1, 5])
        [1, 2, 3, 4, 5]
        >>> remove_duplicates([])
        []
    """
    # Check input type
    if not isinstance(arr, list):
        raise TypeError("Input must be a list")
    
    # Use a set to track seen elements and maintain order
    seen = set()
    result = []
    
    for item in arr:
        if item not in seen:
            seen.add(item)
            result.append(item)
    
    return result