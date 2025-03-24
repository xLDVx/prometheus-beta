import pytest
import logging
from src.length_logger import log_input_length

def test_log_input_length_string(caplog):
    """Test logging length of a string."""
    caplog.set_level(logging.INFO)
    result = log_input_length("hello")
    assert result == 5
    assert "Input length: 5" in caplog.text

def test_log_input_length_list(caplog):
    """Test logging length of a list."""
    caplog.set_level(logging.INFO)
    result = log_input_length([1, 2, 3, 4])
    assert result == 4
    assert "Input length: 4" in caplog.text

def test_log_input_length_empty_string(caplog):
    """Test logging length of an empty string."""
    caplog.set_level(logging.INFO)
    result = log_input_length("")
    assert result == 0
    assert "Input length: 0" in caplog.text

def test_log_input_length_empty_list(caplog):
    """Test logging length of an empty list."""
    caplog.set_level(logging.INFO)
    result = log_input_length([])
    assert result == 0
    assert "Input length: 0" in caplog.text

def test_log_input_length_invalid_type():
    """Test that TypeError is raised for invalid input types."""
    with pytest.raises(TypeError, match="Input must be a string or list"):
        log_input_length(123)

def test_log_input_length_mixed_list(caplog):
    """Test logging length of a mixed-type list."""
    caplog.set_level(logging.INFO)
    result = log_input_length([1, "a", True, None])
    assert result == 4
    assert "Input length: 4" in caplog.text