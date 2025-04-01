import pytest
from datetime import datetime, timedelta
from src.date_subtraction import subtract_days_from_date

def test_subtract_days_from_datetime():
    """Test subtracting days from a datetime object."""
    base_date = datetime(2023, 6, 15)
    result = subtract_days_from_date(base_date, 5)
    assert result == datetime(2023, 6, 10)

def test_subtract_days_from_date_string():
    """Test subtracting days from a date string."""
    base_date = "2023-06-15"
    result = subtract_days_from_date(base_date, 5)
    assert result == datetime(2023, 6, 10)

def test_subtract_zero_days():
    """Test subtracting zero days returns the same date."""
    base_date = datetime(2023, 6, 15)
    result = subtract_days_from_date(base_date, 0)
    assert result == base_date

def test_cross_month_subtraction():
    """Test subtracting days that cross month boundary."""
    base_date = datetime(2023, 5, 10)
    result = subtract_days_from_date(base_date, 15)
    assert result == datetime(2023, 4, 25)

def test_cross_year_subtraction():
    """Test subtracting days that cross year boundary."""
    base_date = datetime(2023, 1, 10)
    result = subtract_days_from_date(base_date, 15)
    assert result == datetime(2022, 12, 26)

def test_invalid_date_type():
    """Test raising TypeError for invalid date type."""
    with pytest.raises(TypeError):
        subtract_days_from_date(123, 5)

def test_invalid_days_type():
    """Test raising TypeError for invalid days type."""
    base_date = datetime(2023, 6, 15)
    with pytest.raises(TypeError):
        subtract_days_from_date(base_date, "5")

def test_negative_days():
    """Test raising ValueError for negative days."""
    base_date = datetime(2023, 6, 15)
    with pytest.raises(ValueError):
        subtract_days_from_date(base_date, -5)

def test_invalid_date_string():
    """Test raising TypeError for invalid date string format."""
    with pytest.raises(TypeError):
        subtract_days_from_date("2023/06/15", 5)