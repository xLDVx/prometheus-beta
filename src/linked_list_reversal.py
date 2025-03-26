class ListNode:
    """
    A class representing a node in a singly linked list.
    
    Attributes:
        val (any): The value stored in the node.
        next (ListNode, optional): Reference to the next node in the list. Defaults to None.
    """
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def reverse_linked_list(head):
    """
    Reverse a singly linked list by changing the direction of node pointers.
    
    Args:
        head (ListNode): The head of the original linked list.
    
    Returns:
        ListNode: The head of the reversed linked list.
    
    Time Complexity: O(n), where n is the number of nodes in the list
    Space Complexity: O(1), as reversal is done in-place
    
    Examples:
        1 -> 2 -> 3 -> None becomes 3 -> 2 -> 1 -> None
        None becomes None
        Single node list remains unchanged
    """
    # Handle edge cases of empty or single-node list
    if not head or not head.next:
        return head
    
    # Initialize three pointers
    prev = None
    current = head
    
    # Iterate through the list and reverse pointers
    while current:
        # Store the next node before changing pointers
        next_node = current.next
        
        # Reverse the current node's pointer
        current.next = prev
        
        # Move pointers forward
        prev = current
        current = next_node
    
    # Return the new head (last node of original list)
    return prev