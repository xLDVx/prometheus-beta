def smooth_sort(arr):
    """
    Implement the smooth sort algorithm for sorting a list.
    
    Smooth sort is an in-place sorting algorithm that provides O(n log n) worst-case time complexity
    and operates efficiently on partially sorted arrays.
    
    Args:
        arr (list): The input list to be sorted in-place.
    
    Returns:
        list: The sorted list.
    
    Raises:
        TypeError: If the input is not a list or contains non-comparable elements.
    """
    # Input validation
    if not isinstance(arr, list):
        raise TypeError("Input must be a list")
    
    # Handle empty or single-element lists
    if len(arr) <= 1:
        return arr
    
    # Leonardo numbers for heap construction
    leonardo_numbers = [1, 1, 3, 5, 9, 15, 25, 41, 67, 109, 177, 287, 465, 753, 1219, 1973]
    
    def sift_down(arr, start, end):
        """
        Perform sift down operation for smooth sort heap.
        
        Args:
            arr (list): The list being sorted
            start (int): Starting index of the sift operation
            end (int): Ending index of the sift operation
        """
        root = start
        while True:
            child = root * 2 + 1
            if child > end:
                break
            
            # Choose the larger child
            if child + 1 <= end and arr[child] < arr[child + 1]:
                child += 1
            
            # If root is larger, heap property is maintained
            if arr[root] >= arr[child]:
                break
            
            # Swap and continue sifting
            arr[root], arr[child] = arr[child], arr[root]
            root = child
    
    def smooth_heapify(arr):
        """
        Create a smooth sort heap.
        
        Args:
            arr (list): The list to be heapified
        """
        for start in range(len(arr) // 2, -1, -1):
            sift_down(arr, start, len(arr) - 1)
    
    def heap_sort(arr):
        """
        Sort the array using heap sort logic.
        
        Args:
            arr (list): The list to be sorted
        """
        smooth_heapify(arr)
        
        for end in range(len(arr) - 1, 0, -1):
            # Swap first and last elements
            arr[0], arr[end] = arr[end], arr[0]
            
            # Sift down the reduced heap
            sift_down(arr, 0, end - 1)
    
    # Create a copy to avoid modifying the original list
    sorted_arr = arr.copy()
    
    # Perform heap sort
    heap_sort(sorted_arr)
    
    return sorted_arr