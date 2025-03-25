def find_list_union(list1, list2):
    """
    Find the union of two lists, removing duplicates and preserving order.

    Args:
        list1 (list): The first input list
        list2 (list): The second input list

    Returns:
        list: A list containing unique elements from both input lists, 
              preserving the order of first occurrence

    Raises:
        TypeError: If input is not a list
    """
    # Validate input types
    if not isinstance(list1, list) or not isinstance(list2, list):
        raise TypeError("Both inputs must be lists")
    
    # Use dict.fromkeys to maintain order and remove duplicates
    return list(dict.fromkeys(list1 + list2))