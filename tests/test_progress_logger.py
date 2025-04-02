import io
import pytest
from src.progress_logger import log_with_progress

def test_basic_iteration():
    """Test basic iteration through a list."""
    items = [1, 2, 3, 4, 5]
    output = io.StringIO()
    result = list(log_with_progress(items, output=output))
    assert result == items
    assert len(output.getvalue()) > 0

def test_iteration_with_description():
    """Test iteration with a custom description."""
    items = [1, 2, 3]
    output = io.StringIO()
    result = list(log_with_progress(items, description="Test", output=output))
    assert result == items
    assert "Test" in output.getvalue()

def test_specific_total():
    """Test iteration with a specified total."""
    items = range(5)
    output = io.StringIO()
    result = list(log_with_progress(items, total=5, output=output))
    assert list(result) == list(range(5))
    assert len(output.getvalue()) > 0

def test_generator_support():
    """Test support for generator objects."""
    def simple_generator():
        for i in range(3):
            yield i
    
    output = io.StringIO()
    result = list(log_with_progress(simple_generator(), output=output))
    assert result == [0, 1, 2]
    assert len(output.getvalue()) > 0

def test_invalid_inputs():
    """Test error handling for invalid inputs."""
    # Test non-iterable input
    with pytest.raises(TypeError):
        list(log_with_progress(42))

def test_empty_iterable():
    """Test behavior with an empty iterable."""
    items = []
    output = io.StringIO()
    result = list(log_with_progress(items, output=output))
    assert result == []
    # Check that some output was generated
    assert len(output.getvalue()) > 0