class TreeNode:
    """
    A class representing a node in a binary tree.
    
    Attributes:
        val (Any): The value stored in the node
        left (TreeNode, optional): Left child node, defaults to None
        right (TreeNode, optional): Right child node, defaults to None
    """
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def tree_traversals(root):
    """
    Perform recursive binary tree traversals and return node values.
    
    Args:
        root (TreeNode): The root of the binary tree
    
    Returns:
        dict: A dictionary containing lists of node values for each traversal type
            - 'pre_order': Pre-order traversal (Root, Left, Right)
            - 'in_order': In-order traversal (Left, Root, Right)
            - 'post_order': Post-order traversal (Left, Right, Root)
    
    Handles edge cases:
    - Returns empty lists for None/empty tree
    - Works with trees of various shapes and sizes
    """
    # Handle empty tree case
    if root is None:
        return {
            'pre_order': [],
            'in_order': [],
            'post_order': []
        }
    
    # Pre-order traversal helper
    def pre_order_traverse(node):
        if node is None:
            return []
        return [node.val] + pre_order_traverse(node.left) + pre_order_traverse(node.right)
    
    # In-order traversal helper
    def in_order_traverse(node):
        if node is None:
            return []
        return in_order_traverse(node.left) + [node.val] + in_order_traverse(node.right)
    
    # Post-order traversal helper
    def post_order_traverse(node):
        if node is None:
            return []
        return post_order_traverse(node.left) + post_order_traverse(node.right) + [node.val]
    
    # Return traversal results
    return {
        'pre_order': pre_order_traverse(root),
        'in_order': in_order_traverse(root),
        'post_order': post_order_traverse(root)
    }