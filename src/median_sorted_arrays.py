def find_median_sorted_arrays(nums1, nums2):
    """
    Find the median of two sorted arrays.
    
    Time complexity: O(log(min(m,n)))
    Space complexity: O(1)
    
    Args:
        nums1 (list): First sorted array of integers
        nums2 (list): Second sorted array of integers
    
    Returns:
        float: Median of the combined sorted arrays
    
    Raises:
        TypeError: If inputs are not lists
        ValueError: If input lists contain non-numeric elements or are unsorted
    """
    # Type checking
    if not isinstance(nums1, list) or not isinstance(nums2, list):
        raise TypeError("Inputs must be lists")
    
    # Validate input contains only numbers
    if not all(isinstance(x, (int, float)) for x in nums1 + nums2):
        raise ValueError("Lists must contain only numeric values")
    
    # Check if arrays are sorted
    if not (all(nums1[i] <= nums1[i+1] for i in range(len(nums1)-1)) and 
            all(nums2[i] <= nums2[i+1] for i in range(len(nums2)-1))):
        raise ValueError("Input arrays must be sorted")
    
    # Ensure nums1 is the smaller array to optimize binary search
    if len(nums1) > len(nums2):
        nums1, nums2 = nums2, nums1
    
    m, n = len(nums1), len(nums2)
    left, right = 0, m
    
    while left <= right:
        # Partition points
        partitionX = (left + right) // 2
        partitionY = (m + n + 1) // 2 - partitionX
        
        # Edge case handling
        maxLeftX = float('-inf') if partitionX == 0 else nums1[partitionX - 1]
        minRightX = float('inf') if partitionX == m else nums1[partitionX]
        
        maxLeftY = float('-inf') if partitionY == 0 else nums2[partitionY - 1]
        minRightY = float('inf') if partitionY == n else nums2[partitionY]
        
        # Check if we have found the correct partition
        if maxLeftX <= minRightY and maxLeftY <= minRightX:
            # Total length is even
            if (m + n) % 2 == 0:
                return (max(maxLeftX, maxLeftY) + min(minRightX, minRightY)) / 2
            # Total length is odd
            else:
                return max(maxLeftX, maxLeftY)
        
        # Adjust binary search
        elif maxLeftX > minRightY:
            right = partitionX - 1
        else:
            left = partitionX + 1
    
    # If no valid partition found (should not reach here due to earlier checks)
    raise ValueError("Unable to find median")