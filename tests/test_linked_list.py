import pytest
from src.linked_list import ListNode, reverse_linked_list

def list_to_array(head):
    """
    Convert a linked list to an array for easy assertion.
    
    Args:
        head (ListNode): Head of the linked list
    
    Returns:
        list: Array representation of the linked list
    """
    result = []
    current = head
    while current:
        result.append(current.val)
        current = current.next
    return result

def array_to_list(arr):
    """
    Convert an array to a linked list.
    
    Args:
        arr (list): Input array
    
    Returns:
        ListNode: Head of the created linked list
    """
    if not arr:
        return None
    
    head = ListNode(arr[0])
    current = head
    
    for val in arr[1:]:
        current.next = ListNode(val)
        current = current.next
    
    return head

def test_reverse_empty_list():
    """Test reversing an empty list."""
    assert reverse_linked_list(None) is None

def test_reverse_single_node_list():
    """Test reversing a list with a single node."""
    head = ListNode(1)
    reversed_head = reverse_linked_list(head)
    assert list_to_array(reversed_head) == [1]

def test_reverse_multiple_node_list():
    """Test reversing a list with multiple nodes."""
    input_arr = [1, 2, 3, 4, 5]
    head = array_to_list(input_arr)
    
    reversed_head = reverse_linked_list(head)
    
    assert list_to_array(reversed_head) == list(reversed(input_arr))

def test_reverse_two_node_list():
    """Test reversing a list with two nodes."""
    input_arr = [1, 2]
    head = array_to_list(input_arr)
    
    reversed_head = reverse_linked_list(head)
    
    assert list_to_array(reversed_head) == list(reversed(input_arr))

def test_linked_list_integrity():
    """Ensure the reversed list maintains node connections."""
    input_arr = [1, 2, 3, 4, 5]
    head = array_to_list(input_arr)
    
    reversed_head = reverse_linked_list(head)
    
    # Verify the list can be traversed completely
    current = reversed_head
    count = 0
    while current:
        count += 1
        current = current.next
    
    assert count == len(input_arr)