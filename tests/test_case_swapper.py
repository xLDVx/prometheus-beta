import pytest
from src.case_swapper import swap_case

def test_swap_case_mixed_string():
    """Test swapping case in a mixed-case string."""
    assert swap_case('Hello World!') == 'hELLO wORLD!'

def test_swap_case_all_lowercase():
    """Test swapping case in an all-lowercase string."""
    assert swap_case('python') == 'PYTHON'

def test_swap_case_all_uppercase():
    """Test swapping case in an all-uppercase string."""
    assert swap_case('PYTHON') == 'python'

def test_swap_case_empty_string():
    """Test swapping case in an empty string."""
    assert swap_case('') == ''

def test_swap_case_with_numbers_and_symbols():
    """Test swapping case with numbers and symbols present."""
    assert swap_case('Hello123!@#') == 'hELLO123!@#'

def test_swap_case_unicode_characters():
    """Test swapping case with Unicode characters."""
    assert swap_case('ÄbcDEF') == 'äBCdef'