import pytest
from src.cartesian_tree_sort import cartesian_tree_sort, build_cartesian_tree, CartesianTreeNode

def test_cartesian_tree_sort_basic():
    """Test basic sorting functionality"""
    arr = [3, 1, 4, 1, 5, 9, 2, 6]
    assert cartesian_tree_sort(arr) == sorted(arr)

def test_cartesian_tree_sort_empty_list():
    """Test sorting an empty list"""
    assert cartesian_tree_sort([]) == []

def test_cartesian_tree_sort_single_element():
    """Test sorting a list with a single element"""
    arr = [42]
    assert cartesian_tree_sort(arr) == arr

def test_cartesian_tree_sort_already_sorted():
    """Test sorting an already sorted list"""
    arr = [1, 2, 3, 4, 5]
    assert cartesian_tree_sort(arr) == arr

def test_cartesian_tree_sort_reverse_sorted():
    """Test sorting a reverse sorted list"""
    arr = [5, 4, 3, 2, 1]
    assert cartesian_tree_sort(arr) == sorted(arr)

def test_cartesian_tree_sort_duplicate_elements():
    """Test sorting a list with duplicate elements"""
    arr = [3, 3, 3, 1, 1, 4]
    assert cartesian_tree_sort(arr) == sorted(arr)

def test_cartesian_tree_sort_negative_numbers():
    """Test sorting a list with negative numbers"""
    arr = [-3, -1, -4, 0, 2, -5]
    assert cartesian_tree_sort(arr) == sorted(arr)

def test_cartesian_tree_sort_mixed_numbers():
    """Test sorting a list with mixed positive and negative numbers"""
    arr = [-10, 5, 0, -3, 7, 2, -5]
    assert cartesian_tree_sort(arr) == sorted(arr)

def test_cartesian_tree_sort_invalid_input():
    """Test that a TypeError is raised for invalid input"""
    with pytest.raises(TypeError):
        cartesian_tree_sort("not a list")

def test_build_cartesian_tree_basic():
    """Test building a basic Cartesian Tree"""
    arr = [3, 1, 4, 1, 5]
    root = build_cartesian_tree(arr)
    
    # Verify the root
    assert root is not None
    assert root.value == 3
    
    # Verify left and right subtrees
    assert root.left is not None
    assert root.left.value == 1
    assert root.right is not None
    assert root.right.value == 4

def test_build_cartesian_tree_empty():
    """Test building a Cartesian Tree from an empty list"""
    assert build_cartesian_tree([]) is None

def test_build_cartesian_tree_invalid_input():
    """Test that a TypeError is raised for invalid input"""
    with pytest.raises(TypeError):
        build_cartesian_tree("not a list")