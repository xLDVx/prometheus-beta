import pytest
from src.number_sorter import sort_numbers_with_even_squares

def test_basic_sorting():
    # Basic test with mixed numbers
    input_list = [3, 1, 2, 4, 5]
    expected = [1, 3, 5, 4, 16]
    assert sort_numbers_with_even_squares(input_list) == expected

def test_all_even_numbers():
    # Test with all even numbers
    input_list = [2, 4, 6, 8]
    expected = [2, 4, 64, 36]
    assert sort_numbers_with_even_squares(input_list) == expected

def test_all_odd_numbers():
    # Test with all odd numbers
    input_list = [1, 3, 5, 7]
    expected = [1, 3, 5, 7]
    assert sort_numbers_with_even_squares(input_list) == expected

def test_empty_list():
    # Test with empty list
    assert sort_numbers_with_even_squares([]) == []

def test_negative_numbers():
    # Test with negative numbers
    input_list = [-2, -1, 0, 1, 2]
    expected = [-2, -1, 0, 1, 4]
    assert sort_numbers_with_even_squares(input_list) == expected

def test_type_error():
    # Test with non-list input
    with pytest.raises(TypeError):
        sort_numbers_with_even_squares("not a list")

def test_value_error():
    # Test with non-numeric list
    with pytest.raises(ValueError):
        sort_numbers_with_even_squares([1, 2, "three", 4])

def test_float_input():
    # Test with float inputs
    input_list = [3.5, 2.0, 1.0, 4.5]
    expected = [1.0, 3.5, 4.5, 4.0]
    assert sort_numbers_with_even_squares(input_list) == expected