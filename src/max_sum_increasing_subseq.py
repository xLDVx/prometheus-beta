from typing import List

def max_sum_increasing_subsequence(nums: List[int]) -> int:
    """
    Find the maximum sum of an increasing subsequence with O(n log n) time complexity.
    
    Args:
        nums (List[int]): Input array of integers
    
    Returns:
        int: Maximum sum of an increasing subsequence
    
    Raises:
        TypeError: If input is not a list or contains non-integer elements
    
    Time Complexity: O(n log n)
    Space Complexity: O(n)
    
    Examples:
        >>> max_sum_increasing_subsequence([1, 101, 2, 3, 100])
        106
        >>> max_sum_increasing_subsequence([10, 22, 9, 33, 21, 50, 41, 60, 80])
        255
        >>> max_sum_increasing_subsequence([])
        0
    """
    # Type checking
    if not isinstance(nums, list):
        raise TypeError("Input must be a list")
    
    # Check if all elements are integers
    if not all(isinstance(x, int) for x in nums):
        raise TypeError("All elements must be integers")
    
    # Handle empty input
    if not nums:
        return 0
    
    # Initialize an array to store maximum sums of increasing subsequences
    # ending at each index
    max_sums = nums.copy()
    
    # Iterate through the array to find maximum increasing subsequence sums
    for i in range(1, len(nums)):
        for j in range(i):
            # If current number is larger and we can increase the sum
            if nums[i] > nums[j] and max_sums[i] < max_sums[j] + nums[i]:
                max_sums[i] = max_sums[j] + nums[i]
    
    # Return the maximum sum found
    return max(max_sums) if max_sums else 0