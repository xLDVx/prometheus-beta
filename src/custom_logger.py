import typing
import termcolor

def log_message(message: str, 
                color: str = 'white', 
                background: typing.Optional[str] = None, 
                attrs: typing.Optional[list[str]] = None) -> None:
    """
    Log a message with custom styling using termcolor.

    Args:
        message (str): The message to log
        color (str, optional): Text color. Defaults to 'white'.
        background (str, optional): Background color. Defaults to None.
        attrs (list[str], optional): Text attributes like 'bold', 'underline'. Defaults to None.

    Raises:
        ValueError: If an invalid color or attribute is provided
        TypeError: If inputs are of incorrect type

    Example:
        log_message("Hello, World!", color='green', attrs=['bold'])
    """
    # Validate inputs
    valid_colors = ['grey', 'red', 'green', 'yellow', 'blue', 'magenta', 'cyan', 'white']
    valid_attrs = ['bold', 'dark', 'underline', 'blink', 'reverse', 'concealed']

    # Type checking
    if not isinstance(message, str):
        raise TypeError("Message must be a string")
    
    if color not in valid_colors:
        raise ValueError(f"Invalid color. Must be one of {valid_colors}")
    
    if background is not None and background not in valid_colors:
        raise ValueError(f"Invalid background color. Must be one of {valid_colors}")
    
    if attrs is not None:
        if not isinstance(attrs, list):
            raise TypeError("Attributes must be a list")
        for attr in attrs:
            if attr not in valid_attrs:
                raise ValueError(f"Invalid attribute: {attr}. Must be one of {valid_attrs}")

    # Use termcolor to print styled message
    print(termcolor.colored(message, color, on_color=f'on_{background}' if background else None, attrs=attrs))