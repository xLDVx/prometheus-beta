import pytest
from src.linked_list_reversal import ListNode, reverse_linked_list

def create_linked_list(values):
    """
    Helper function to create a linked list from a list of values.
    
    Args:
        values (list): List of values to create linked list from.
    
    Returns:
        ListNode: Head of the created linked list.
    """
    if not values:
        return None
    
    head = ListNode(values[0])
    current = head
    
    for val in values[1:]:
        current.next = ListNode(val)
        current = current.next
    
    return head

def linked_list_to_list(head):
    """
    Convert a linked list to a regular list for easy comparison.
    
    Args:
        head (ListNode): Head of the linked list.
    
    Returns:
        list: List representation of the linked list values.
    """
    result = []
    current = head
    
    while current:
        result.append(current.val)
        current = current.next
    
    return result

def test_reverse_empty_list():
    """Test reversing an empty list."""
    assert reverse_linked_list(None) is None

def test_reverse_single_node_list():
    """Test reversing a single-node list."""
    head = ListNode(1)
    reversed_head = reverse_linked_list(head)
    assert linked_list_to_list(reversed_head) == [1]

def test_reverse_multiple_node_list():
    """Test reversing a multi-node list."""
    values = [1, 2, 3, 4, 5]
    head = create_linked_list(values)
    reversed_head = reverse_linked_list(head)
    assert linked_list_to_list(reversed_head) == list(reversed(values))

def test_reverse_two_node_list():
    """Test reversing a two-node list."""
    values = [1, 2]
    head = create_linked_list(values)
    reversed_head = reverse_linked_list(head)
    assert linked_list_to_list(reversed_head) == list(reversed(values))

def test_reverse_preserves_original_list_structure():
    """Ensure that the reversal actually changes pointer directions."""
    values = [1, 2, 3, 4, 5]
    head = create_linked_list(values)
    reversed_head = reverse_linked_list(head)
    
    # Check that the first node of the reversed list is the last of the original
    assert reversed_head.val == values[-1]
    
    # Verify pointer redirection
    current = reversed_head
    for expected_val in reversed(values):
        assert current.val == expected_val
        current = current.next