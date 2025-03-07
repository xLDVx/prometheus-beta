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
    
    # Create nodes for the array
    nodes = [CartesianTreeNode(val) for val in arr]
    
    # Track parent for each node
    parent = [None] * len(arr)
    
    # For each node, find its parent in the Cartesian Tree
    for i in range(1, len(arr)):
        j = i - 1
        
        # Move j to find the right place for the current node
        while j >= 0 and nodes[j].value >= nodes[i].value:
            j = parent[j] is not None and parent[j] or j - 1
        
        # Update node connections
        if j >= 0:
            # If parent node exists, current node goes to its right
            nodes[j].right = nodes[i]
            parent[i] = j
        else:
            # If no suitable parent, the current node becomes the first node
            if parent[0] is not None:
                nodes[i].left = nodes[0]
            parent[0] = i
    
    # Find the root node
    root_idx = 0
    while parent[root_idx] is not None:
        root_idx = parent[root_idx]
    
    return nodes[root_idx]

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