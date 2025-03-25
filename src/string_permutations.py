def generate_unique_permutations(input_string):
    """
    Generate all possible unique permutations of a given string.
    
    Args:
        input_string (str): The input string to generate permutations for.
    
    Returns:
        list: A list of unique permutations of the input string.
    
    Raises:
        TypeError: If input is not a string.
    """
    # Validate input
    if not isinstance(input_string, str):
        raise TypeError("Input must be a string")
    
    # Handle empty string edge case
    if not input_string:
        return []
    
    # Convert to list for easier manipulation
    chars = list(input_string)
    
    # Use a set to store unique permutations
    unique_permutations = set()
    
    def backtrack(start):
        """
        Recursive backtracking to generate permutations.
        
        Args:
            start (int): Starting index for current permutation generation.
        """
        # If we've reached the end of the string, add the current permutation
        if start == len(chars):
            unique_permutations.add(''.join(chars))
            return
        
        # Generate permutations by swapping current char with subsequent chars
        for i in range(start, len(chars)):
            # Swap characters
            chars[start], chars[i] = chars[i], chars[start]
            
            # Recurse to generate permutations for the rest of the string
            backtrack(start + 1)
            
            # Backtrack (undo the swap)
            chars[start], chars[i] = chars[i], chars[start]
    
    # Start the permutation generation
    backtrack(0)
    
    # Convert set to sorted list for consistent output
    return sorted(list(unique_permutations))