import logging
from typing import Union, List, Any

def log_input_length(input_value: Union[str, List[Any]]) -> int:
    """
    Log the length of a given string or array and return the length.

    Args:
        input_value (str or List): The input to measure the length of.

    Returns:
        int: The length of the input.

    Raises:
        TypeError: If the input is not a string or list.
    """
    # Validate input type
    if not isinstance(input_value, (str, list)):
        raise TypeError("Input must be a string or list")

    # Get the length of the input
    length = len(input_value)

    # Log the length using the logging module
    logging.info(f"Input length: {length}")

    return length