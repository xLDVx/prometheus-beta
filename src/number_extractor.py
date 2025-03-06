import re
from typing import List, Union

def extract_numbers(input_string: str) -> List[Union[int, float]]:
    """
    Extract all numeric values (integers and floats) from a given string.
    
    Args:
        input_string (str): The input string to extract numbers from.
    
    Returns:
        List[Union[int, float]]: A list of extracted numbers.
    
    Examples:
        >>> extract_numbers("I have 42 apples and 3.14 pies")
        [42, 3.14]
        >>> extract_numbers("No numbers here")
        []
    """
    # Regular expression to match integers and floating-point numbers
    number_pattern = r'-?\d+(?:\.\d+)?'
    
    # Find all matches and convert to appropriate numeric type
    extracted = []
    for match in re.findall(number_pattern, input_string):
        # Try to convert to int first, if that fails, convert to float
        try:
            num = int(match)
        except ValueError:
            num = float(match)
        extracted.append(num)
    
    return extracted