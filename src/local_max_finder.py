from typing import List, Optional


def find_local_max_values(arr: List[int]) -> List[int]:
    """
    Find local maximum values in an input array.
    
    A local maximum is defined as an element that is strictly greater than 
    its immediate neighboring elements. For the first and last elements, 
    they are considered local maximums if they are greater than their 
    single adjacent neighbor.
    
    Args:
        arr (List[int]): Input array of integers
    
    Returns:
        List[int]: List of local maximum values
    
    Raises:
        TypeError: If input is not a list
        ValueError: If input list is empty
    
    Examples:
        >>> find_local_max_values([1, 3, 2, 4, 1, 5])
        [3, 4, 5]
        >>> find_local_max_values([1, 2, 3, 4, 5])
        [5]
        >>> find_local_max_values([5, 4, 3, 2, 1])
        [5]
    """
    # Validate input
    if not isinstance(arr, list):
        raise TypeError("Input must be a list")
    
    if len(arr) == 0:
        raise ValueError("Input list cannot be empty")
    
    # Handle single element case
    if len(arr) == 1:
        return arr
    
    # Find local maximums
    local_max = []
    
    # Check first element
    if arr[0] > arr[1]:
        local_max.append(arr[0])
    
    # Check middle elements
    for i in range(1, len(arr) - 1):
        if arr[i] > arr[i-1] and arr[i] > arr[i+1]:
            local_max.append(arr[i])
    
    # Check last element
    if arr[-1] > arr[-2]:
        local_max.append(arr[-1])
    
    # Special case: if no local max found and all equal, return first/last
    if not local_max and len(set(arr)) == 1:
        local_max.append(arr[0])
    
    return local_max