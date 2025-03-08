def find_palindrome_pairs(words):
    """
    Find all pairs of indices where concatenation of words forms a palindrome.
    
    Args:
        words (list): A list of strings to check for palindrome pairs.
    
    Returns:
        list: A list of tuples containing pairs of indices where 
              words[i] + words[j] or words[j] + words[i] form a palindrome.
    
    Time Complexity: O(n^2 * m), where n is the number of words 
                     and m is the length of the longest word.
    Space Complexity: O(n^2)
    
    Edge Cases:
    - Returns empty list for empty input
    - Handles single character words
    - Checks both forward and reverse concatenations
    """
    def is_palindrome(s):
        """Check if a string is a palindrome."""
        return s == s[::-1]
    
    # Validate input
    if not words or not isinstance(words, list):
        return []
    
    # Result to store palindrome pairs
    palindrome_pairs = []
    
    # Check all possible pairs
    for i in range(len(words)):
        for j in range(len(words)):
            # Skip same index
            if i == j:
                continue
            
            # Check concatenation in both directions
            if is_palindrome(words[i] + words[j]):
                palindrome_pairs.append((i, j))
    
    return palindrome_pairs