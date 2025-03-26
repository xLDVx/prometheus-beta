def longest_palindromic_substring(s: str) -> str:
    """
    Find the longest palindromic substring in the given string.
    
    A palindrome is a string that reads the same backward as forward.
    
    Args:
        s (str): Input string to search for palindromic substrings
    
    Returns:
        str: The longest palindromic substring
    
    Time Complexity: O(n^2)
    Space Complexity: O(1)
    
    Edge Cases:
    - Empty string returns empty string
    - Single character is a palindrome
    - Multiple palindromes of same length will return first occurrence
    
    Examples:
        >>> longest_palindromic_substring("babad")
        'bab'
        >>> longest_palindromic_substring("cbbd")
        'bb'
        >>> longest_palindromic_substring("")
        ''
    """
    # Handle edge cases
    if not s or len(s) < 1:
        return ""
    
    # If length is 1, return the string
    if len(s) == 1:
        return s
    
    start, max_length = 0, 0
    
    def expand_around_center(left: int, right: int) -> int:
        """
        Expand around center and return length of palindrome
        """
        while left >= 0 and right < len(s) and s[left] == s[right]:
            left -= 1
            right += 1
        return right - left - 1
    
    # Iterate through each character as potential center
    for i in range(len(s)):
        # Check odd length palindromes
        length1 = expand_around_center(i, i)
        
        # Check even length palindromes
        length2 = expand_around_center(i, i + 1)
        
        # Choose the maximum length
        curr_max_length = max(length1, length2)
        
        # Update start and max_length if needed
        if curr_max_length > max_length:
            start = i - (curr_max_length - 1) // 2
            max_length = curr_max_length
    
    return s[start:start + max_length]