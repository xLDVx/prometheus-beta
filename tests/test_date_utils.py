import pytest
from datetime import datetime, timedelta
from src.date_utils import add_days_to_date


def test_add_days_to_datetime():
    """Test adding days to a datetime object."""
    base_date = datetime(2023, 1, 1)
    result = add_days_to_date(base_date, 5)
    assert result == datetime(2023, 1, 6)


def test_add_days_to_date_string():
    """Test adding days to a date string."""
    result = add_days_to_date('2023-01-01', 5)
    assert result == datetime(2023, 1, 6)


def test_subtract_days():
    """Test subtracting days using negative number."""
    base_date = datetime(2023, 1, 10)
    result = add_days_to_date(base_date, -5)
    assert result == datetime(2023, 1, 5)


def test_cross_month_boundary():
    """Test adding days that cross a month boundary."""
    base_date = datetime(2023, 1, 30)
    result = add_days_to_date(base_date, 5)
    assert result == datetime(2023, 2, 4)


def test_cross_year_boundary():
    """Test adding days that cross a year boundary."""
    base_date = datetime(2023, 12, 30)
    result = add_days_to_date(base_date, 5)
    assert result == datetime(2024, 1, 4)


def test_invalid_date_string():
    """Test with an incorrectly formatted date string."""
    with pytest.raises(ValueError, match="Date string must be in 'YYYY-MM-DD' format"):
        add_days_to_date('01-01-2023', 5)


def test_invalid_days_type():
    """Test with non-integer days input."""
    with pytest.raises(ValueError, match="Days must be an integer"):
        add_days_to_date(datetime(2023, 1, 1), '5')


def test_invalid_date_type():
    """Test with invalid date type."""
    with pytest.raises(TypeError, match="Date must be a datetime object or a string in 'YYYY-MM-DD' format"):
        add_days_to_date(123, 5)