import pytest
import io
import sys
from termcolor import colored
from src.custom_logger import log_message

def test_log_message_default():
    # Capture stdout
    captured_output = io.StringIO()
    sys.stdout = captured_output

    # Call the function
    log_message("Test Message")

    # Reset redirect
    sys.stdout = sys.__stdout__

    # Check the output contains the original message
    assert "Test Message" in captured_output.getvalue()

def test_log_message_with_color():
    captured_output = io.StringIO()
    sys.stdout = captured_output

    log_message("Green Message", color='green')

    sys.stdout = sys.__stdout__

    # Verify the message contains color-specific escape sequence
    assert colored("Green Message", 'green') in captured_output.getvalue()

def test_log_message_with_background():
    captured_output = io.StringIO()
    sys.stdout = captured_output

    log_message("Red on Yellow", color='red', background='yellow')

    sys.stdout = sys.__stdout__

    # Verify the message contains color-specific escape sequence
    assert colored("Red on Yellow", 'red', on_color='on_yellow') in captured_output.getvalue()

def test_log_message_with_attributes():
    captured_output = io.StringIO()
    sys.stdout = captured_output

    log_message("Bold Underline", color='blue', attrs=['bold', 'underline'])

    sys.stdout = sys.__stdout__

    # Verify the message contains the correct attributes
    assert colored("Bold Underline", 'blue', attrs=['bold', 'underline']) in captured_output.getvalue()

def test_invalid_color():
    with pytest.raises(ValueError, match="Invalid color"):
        log_message("Invalid Color", color='invalid_color')

def test_invalid_background():
    with pytest.raises(ValueError, match="Invalid background color"):
        log_message("Invalid Background", background='invalid_background')

def test_invalid_attributes():
    with pytest.raises(ValueError, match="Invalid attribute"):
        log_message("Invalid Attribute", attrs=['super_invalid'])

def test_invalid_message_type():
    with pytest.raises(TypeError, match="Message must be a string"):
        log_message(123)

def test_invalid_attributes_type():
    with pytest.raises(TypeError, match="Attributes must be a list"):
        log_message("Test", attrs="not a list")