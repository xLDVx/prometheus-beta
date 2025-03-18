import pytest
from src.prime_filter import filter_primes

def test_filter_primes_basic():
    """Test filtering prime numbers from a mixed list"""
    input_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    assert filter_primes(input_list) == [2, 3, 5, 7]

def test_filter_primes_empty_list():
    """Test filtering an empty list"""
    assert filter_primes([]) == []

def test_filter_primes_no_primes():
    """Test list with no prime numbers"""
    assert filter_primes([1, 4, 6, 8, 9, 10]) == []

def test_filter_primes_all_primes():
    """Test list with all prime numbers"""
    assert filter_primes([2, 3, 5, 7, 11, 13]) == [2, 3, 5, 7, 11, 13]

def test_filter_primes_with_negatives():
    """Test handling of negative numbers"""
    input_list = [-7, -5, -3, -2, -1, 0, 1, 2, 3, 4, 5, 6, 7]
    assert filter_primes(input_list) == [2, 3, 5, 7]

def test_filter_primes_large_numbers():
    """Test filtering larger prime numbers"""
    input_list = [97, 100, 541, 600, 1009]
    assert filter_primes(input_list) == [97, 541, 1009]

def test_filter_primes_zero_and_one():
    """Verify that 0 and 1 are not considered prime"""
    assert filter_primes([0, 1, 2, 3]) == [2, 3]