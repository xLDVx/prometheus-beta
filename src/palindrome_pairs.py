def find_palindrome_pairs(words):
    """
    Find all pairs of indices in an array of strings where concatenated strings form a palindrome.
    
    Args:
        words (List[str]): A list of strings to check for palindrome pairs.
    
    Returns:
        List[List[int]]: A list of pairs of indices where words[i] + words[j] forms a palindrome.
    
    Time Complexity: O(n^2 * k), where n is the number of words and k is the max word length
    Space Complexity: O(n^2) to store the result pairs
    
    Examples:
        >>> find_palindrome_pairs(["abcd", "dcba", "lls", "s", "sssll"])
        [[0, 1], [1, 0], [3, 4], [4, 3]]
    """
    def is_palindrome(s):
        """Helper function to check if a string is a palindrome."""
        return s == s[::-1]
    
    # Input validation
    if not words or not isinstance(words, list) or len(words) < 2:
        return []
    
    # Result to store palindrome pairs
    palindrome_pairs = []
    
    # Check all possible pairs of words
    for i in range(len(words)):
        for j in range(len(words)):
            # Skip same index
            if i == j:
                continue
            
            # Check both left and right concatenation for palindrome
            concat1 = words[i] + words[j]
            concat2 = words[j] + words[i]
            
            if is_palindrome(concat1):
                palindrome_pairs.append([i, j])
            
    return list(set(tuple(x) for x in palindrome_pairs))