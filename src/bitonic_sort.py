def bitonic_sort(arr, ascending=True):
    """
    Implement the bitonic sort algorithm.
    
    Bitonic sort is a comparison-based sorting algorithm that can sort 
    arrays of size 2^n efficiently. It works by creating a bitonic sequence 
    and then merging it in the desired order.
    
    Args:
        arr (list): The input list to be sorted
        ascending (bool, optional): Sort in ascending order if True, 
                                    descending order if False. Defaults to True.
    
    Returns:
        list: A new sorted list
    
    Raises:
        TypeError: If input is not a list
        ValueError: If list length is not a power of 2
    """
    # Validate input
    if not isinstance(arr, list):
        raise TypeError("Input must be a list")
    
    # Check if list length is a power of 2
    if not (len(arr) > 0 and (len(arr) & (len(arr) - 1)) == 0):
        raise ValueError("List length must be a power of 2")
    
    def compare_and_swap(arr, i, j, direction):
        """
        Compare and potentially swap elements based on the direction.
        
        Args:
            arr (list): The list being sorted
            i (int): First index to compare
            j (int): Second index to compare
            direction (bool): True for ascending, False for descending
        """
        if direction == (arr[i] > arr[j]):
            arr[i], arr[j] = arr[j], arr[i]
    
    def bitonic_merge(arr, low, count, direction):
        """
        Merge a bitonic sequence.
        
        Args:
            arr (list): The list being sorted
            low (int): Starting index of the sequence
            count (int): Number of elements to merge
            direction (bool): True for ascending, False for descending
        """
        if count > 1:
            k = count // 2
            for i in range(low, low + k):
                compare_and_swap(arr, i, i + k, direction)
            
            bitonic_merge(arr, low, k, direction)
            bitonic_merge(arr, low + k, k, direction)
    
    def bitonic_sort_recursive(arr, low, count, direction):
        """
        Recursively sort the bitonic sequence.
        
        Args:
            arr (list): The list being sorted
            low (int): Starting index of the sequence
            count (int): Number of elements to sort
            direction (bool): True for ascending, False for descending
        """
        if count > 1:
            k = count // 2
            
            # Sort first half in ascending order
            bitonic_sort_recursive(arr, low, k, True)
            
            # Sort second half in descending order
            bitonic_sort_recursive(arr, low + k, k, False)
            
            # Merge the entire sequence
            bitonic_merge(arr, low, count, direction)
    
    # Create a copy to avoid modifying the original list
    sorted_arr = arr.copy()
    
    # Perform bitonic sort
    bitonic_sort_recursive(sorted_arr, 0, len(sorted_arr), ascending)
    
    return sorted_arr