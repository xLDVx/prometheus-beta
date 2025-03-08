class ListNode:
    """
    A class representing a node in a singly linked list.
    
    Attributes:
        val: The value stored in the node
        next: Reference to the next node in the list (None if last node)
    """
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def reverse_linked_list(head):
    """
    Reverses a singly linked list and returns the new head.
    
    Args:
        head (ListNode): The head of the input linked list
    
    Returns:
        ListNode: The head of the reversed linked list
    
    Time Complexity: O(n)
    Space Complexity: O(1)
    """
    # Handle empty list or single node list
    if not head or not head.next:
        return head
    
    # Initialize three pointers
    prev = None
    current = head
    
    # Iterate through the list and reverse links
    while current:
        # Store next node before changing links
        next_node = current.next
        
        # Reverse the link
        current.next = prev
        
        # Move pointers forward
        prev = current
        current = next_node
    
    # Return the new head (last node of original list)
    return prev