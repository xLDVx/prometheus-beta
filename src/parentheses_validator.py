def is_balanced_parentheses(s: str) -> bool:
    """
    Check if all parentheses in the given string are balanced.
    
    Args:
        s (str): Input string to check for balanced parentheses.
    
    Returns:
        bool: True if all parentheses are balanced, False otherwise.
    
    Examples:
        >>> is_balanced_parentheses("()")  # Simple balanced case
        True
        >>> is_balanced_parentheses("((()))")  # Nested balanced case
        True
        >>> is_balanced_parentheses("(()())")  # Multiple sets balanced
        True
        >>> is_balanced_parentheses("(()")  # Unbalanced case
        False
        >>> is_balanced_parentheses(")(")  # Invalid order
        False
    """
    # Stack to keep track of opening parentheses
    stack = []
    
    # Dictionary of matching parentheses pairs
    pairs = {')': '(', '}': '{', ']': '['}
    
    # Set of opening parentheses
    opening = set(pairs.values())
    
    for char in s:
        # If it's an opening parenthesis, push to stack
        if char in opening:
            stack.append(char)
        
        # If it's a closing parenthesis
        elif char in pairs:
            # If stack is empty or top doesn't match, it's unbalanced
            if not stack or stack[-1] != pairs[char]:
                return False
            
            # Remove the matching opening parenthesis
            stack.pop()
    
    # Stack should be empty for perfectly balanced parentheses
    return len(stack) == 0