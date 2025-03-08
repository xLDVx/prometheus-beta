import pytest
from src.max_sum_increasing_subseq import max_sum_increasing_subsequence

def test_max_sum_increasing_subsequence_basic():
    """Test basic scenarios of maximum sum increasing subsequence."""
    assert max_sum_increasing_subsequence([1, 101, 2, 3, 100]) == 106
    assert max_sum_increasing_subsequence([10, 22, 9, 33, 21, 50, 41, 60, 80]) == 255

def test_max_sum_increasing_subsequence_edge_cases():
    """Test edge cases including empty list and single element."""
    assert max_sum_increasing_subsequence([]) == 0
    assert max_sum_increasing_subsequence([5]) == 5
    assert max_sum_increasing_subsequence([-1, -2, -3]) == -1

def test_max_sum_increasing_subsequence_complex_scenarios():
    """Test more complex scenarios of increasing subsequences."""
    assert max_sum_increasing_subsequence([3, 4, 5, 1]) == 12
    assert max_sum_increasing_subsequence([10, 5, 4, 3]) == 10
    assert max_sum_increasing_subsequence([1, 2, 3, 4, 5]) == 15

def test_max_sum_increasing_subsequence_mixed_numbers():
    """Test scenarios with mixed positive and negative numbers."""
    assert max_sum_increasing_subsequence([-2, 1, -3, 4, -1, 2, 1, -5, 4]) == 7
    assert max_sum_increasing_subsequence([1, -1, 2, -2, 3]) == 4

def test_input_types():
    """Ensure the function handles different input types correctly."""
    with pytest.raises(TypeError):
        max_sum_increasing_subsequence("not a list")
    with pytest.raises(TypeError):
        max_sum_increasing_subsequence([1, 2, "3"])