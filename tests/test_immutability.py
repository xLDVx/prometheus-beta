def test_input_array_immutability():
    """Test that the original input array remains unchanged"""
    original = [1, 2, 3, 4, 5]
    from src.double_even_numbers import double_even_numbers
    result = double_even_numbers(original)
    
    # Verify the original array is unchanged
    assert original == [1, 2, 3, 4, 5], "Original array should not be modified"
    
    # Verify the result is a new array
    assert result is not original, "Function should return a new array"