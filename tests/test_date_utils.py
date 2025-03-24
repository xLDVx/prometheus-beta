import pytest
from datetime import date, timedelta
from src.date_utils import calculate_days_between_dates

def test_calculate_days_between_dates_same_date():
    """Test calculating days between the same date"""
    assert calculate_days_between_dates('2023-01-01', '2023-01-01') == 0

def test_calculate_days_between_dates_different_dates():
    """Test calculating days between different dates"""
    assert calculate_days_between_dates('2023-01-01', '2023-01-10') == 9
    assert calculate_days_between_dates('2023-01-10', '2023-01-01') == 9

def test_calculate_days_between_dates_date_objects():
    """Test calculating days using date objects"""
    date1 = date(2023, 1, 1)
    date2 = date(2023, 1, 10)
    assert calculate_days_between_dates(date1, date2) == 9

def test_calculate_days_between_dates_across_years():
    """Test calculating days across different years"""
    assert calculate_days_between_dates('2022-12-31', '2023-01-01') == 1

def test_calculate_days_between_dates_invalid_string_format():
    """Test handling of invalid date string formats"""
    with pytest.raises(ValueError, match="Invalid date format"):
        calculate_days_between_dates('01-01-2023', '2023-01-10')

def test_calculate_days_between_dates_invalid_input_type():
    """Test handling of invalid input types"""
    with pytest.raises(ValueError, match="Inputs must be date objects"):
        calculate_days_between_dates(123, '2023-01-10')

def test_calculate_days_between_dates_leap_year():
    """Test calculation including a leap year"""
    assert calculate_days_between_dates('2020-02-28', '2020-03-01') == 2