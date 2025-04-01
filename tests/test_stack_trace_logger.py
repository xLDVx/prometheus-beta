import logging
import pytest
from src.stack_trace_logger import log_stack_trace

# Create a custom logger for testing
test_logger = logging.getLogger('test_logger')
test_handler = logging.Handler()
test_handler.records = []

def custom_emit(record):
    test_handler.records.append(record)

test_handler.emit = custom_emit
test_logger.addHandler(test_handler)
test_logger.setLevel(logging.DEBUG)

def test_log_stack_trace_with_exception():
    # Create a test exception
    try:
        raise ValueError("Test exception")
    except ValueError as e:
        # Clear previous records
        test_handler.records.clear()
        
        # Log the stack trace
        trace_str = log_stack_trace(e, logger=test_logger)
        
        # Verify logging
        assert len(test_handler.records) == 1
        assert "Test exception" in trace_str
        assert "test_log_stack_trace_with_exception" in trace_str

def test_log_stack_trace_current_exception():
    try:
        raise RuntimeError("Current exception test")
    except RuntimeError:
        # Clear previous records
        test_handler.records.clear()
        
        # Log the stack trace
        trace_str = log_stack_trace(logger=test_logger)
        
        # Verify logging
        assert len(test_handler.records) == 1
        assert "Current exception test" in trace_str
        assert "test_log_stack_trace_current_exception" in trace_str

def test_log_stack_trace_no_exception():
    # Clear previous records
    test_handler.records.clear()
    
    # Verify that calling without an exception raises ValueError
    with pytest.raises(ValueError, match="No exception found to trace"):
        log_stack_trace(logger=test_logger)

def test_log_stack_trace_custom_log_level():
    try:
        raise TypeError("Custom log level test")
    except TypeError as e:
        # Clear previous records
        test_handler.records.clear()
        
        # Log with a different log level
        trace_str = log_stack_trace(e, logger=test_logger, log_level=logging.CRITICAL)
        
        # Verify logging
        assert len(test_handler.records) == 1
        assert test_handler.records[0].levelno == logging.CRITICAL
        assert "Custom log level test" in trace_str