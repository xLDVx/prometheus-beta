import traceback
import logging
import sys
from typing import Optional, Union, Callable, Any

def log_stack_trace(
    exception: Optional[Union[Exception, BaseException]] = None, 
    logger: Optional[logging.Logger] = None, 
    log_level: int = logging.ERROR
) -> str:
    """
    Log a stack trace with optional customization.

    Args:
        exception (Optional[Exception]): The exception to log. If None, uses the current exception.
        logger (Optional[logging.Logger]): Logger to use. If None, uses root logger.
        log_level (int): Logging level to use. Defaults to logging.ERROR.

    Returns:
        str: The formatted stack trace as a string.

    Raises:
        ValueError: If no exception is available to trace.
    """
    # If no logger provided, use root logger
    if logger is None:
        logger = logging.getLogger()

    # Determine the stack trace
    if exception:
        # If an exception is provided, use its traceback
        trace = traceback.format_exception(type(exception), exception, exception.__traceback__)
    else:
        # If no exception provided, try to get the current exception
        exc_info = sys.exc_info()
        if exc_info[0] is None:
            raise ValueError("No exception found to trace. Provide an exception or call within an except block.")
        trace = traceback.format_exception(*exc_info)

    # Convert trace to a single string
    trace_str = ''.join(trace)

    # Log the stack trace
    logger.log(log_level, trace_str)

    return trace_str