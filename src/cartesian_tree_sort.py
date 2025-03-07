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
    
    The Cartesian Tree property requires:
    1. It is a binary tree
    2. The heap property: parent.value is min/max compared to children
    3. In-order traversal gives the original array
    
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
    
    def build_tree(start: int, end: int) -> Optional[CartesianTreeNode]:
        """
        Recursively build the Cartesian Tree.
        
        Args:
            start: Start index of the subarray
            end: End index of the subarray
        
        Returns:
            Root of the subtree
        """
        if start > end:
            return None
        
        # Find the index with the minimum value in the range
        min_idx = start
        for i in range(start + 1, end + 1):
            if arr[i] < arr[min_idx]:
                min_idx = i
        
        # Create root node with minimum value
        root = CartesianTreeNode(arr[min_idx])
        
        # Recursively build left and right subtrees
        root.left = build_tree(start, min_idx - 1)
        root.right = build_tree(min_idx + 1, end)
        
        return root
    
    # Build and return the full Cartesian Tree
    return build_tree(0, len(arr) - 1)

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