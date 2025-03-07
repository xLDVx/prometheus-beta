from typing import List, TypeVar, Optional

T = TypeVar('T')

class CartesianTreeNode:
    """
    Node class for Cartesian Tree representation.
    
    Attributes:
        value: The value stored in the node
        left: Left child node
        right: Right child node
    """
    def __init__(self, value: T):
        """
        Initialize a Cartesian Tree Node.
        
        Args:
            value: The value to be stored in the node
        """
        self.value = value
        self.left: Optional[CartesianTreeNode] = None
        self.right: Optional[CartesianTreeNode] = None

def build_cartesian_tree(arr: List[T]) -> Optional[CartesianTreeNode]:
    """
    Build a Cartesian Tree from a given array.
    
    Args:
        arr: Input list to build the Cartesian Tree from
    
    Returns:
        Root of the Cartesian Tree, or None for empty input
    
    Raises:
        TypeError: If input is not a list
    """
    # Input validation
    if not isinstance(arr, list):
        raise TypeError("Input must be a list")
    
    # Handle empty list
    if not arr:
        return None
    
    # Create a stack to build the Cartesian Tree
    stack: List[CartesianTreeNode] = []
    
    for num in arr:
        # Create a new node for the current element
        node = CartesianTreeNode(num)
        
        # Find the rightmost node that should be the parent of current node
        while stack and stack[-1].value > num:
            node.left = stack.pop()
        
        # If stack is not empty, the last node is the parent of current node
        if stack:
            stack[-1].right = node
        
        # Push current node to stack
        stack.append(node)
    
    # The last node in stack is the root of the Cartesian Tree
    return stack[0]

def cartesian_tree_sort(arr: List[T]) -> List[T]:
    """
    Sort an input list using Cartesian Tree Sort algorithm.
    
    Args:
        arr: Input list to be sorted
    
    Returns:
        Sorted list
    
    Raises:
        TypeError: If input is not a list
    """
    # Build Cartesian Tree
    root = build_cartesian_tree(arr)
    
    # If root is None (empty list), return empty list
    if root is None:
        return []
    
    # Perform in-order traversal to get sorted list
    def in_order_traversal(node: Optional[CartesianTreeNode]) -> List[T]:
        """
        Perform in-order traversal of Cartesian Tree.
        
        Args:
            node: Current node in the traversal
        
        Returns:
            List of values in sorted order
        """
        if node is None:
            return []
        
        return (in_order_traversal(node.left) + 
                [node.value] + 
                in_order_traversal(node.right))
    
    return in_order_traversal(root)