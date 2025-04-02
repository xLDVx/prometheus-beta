import sys
from tqdm import tqdm
from typing import Iterable, Optional, TextIO, Generator, Any

def log_with_progress(
    items: Iterable[Any], 
    description: Optional[str] = None, 
    total: Optional[int] = None, 
    output: Optional[TextIO] = None
) -> Generator[Any, None, None]:
    """
    Create a dynamic progress bar logger for iterating through items.

    Args:
        items (Iterable): The collection of items to iterate through
        description (Optional[str]): Description of the progress bar
        total (Optional[int]): Total number of items (if known)
        output (Optional[TextIO]): Output stream for progress bar (default: sys.stderr)

    Yields:
        Each item from the input iterable

    Raises:
        TypeError: If items is not iterable
        ValueError: If total is less than or equal to 0 when specified
    """
    # Validate inputs
    if not hasattr(items, '__iter__'):
        raise TypeError("Input must be an iterable")
    
    # Determine total if not specified
    if total is None:
        try:
            total = len(items)
        except TypeError:
            total = None
    
    # Validate total if specified
    if total is not None and total <= 0:
        raise ValueError("Total must be a positive integer")
    
    # Use specified output or default to stderr
    output = output or sys.stderr
    
    # Create tqdm progress bar
    with tqdm(
        items, 
        total=total, 
        desc=description, 
        file=output, 
        dynamic_ncols=True
    ) as progress_bar:
        for item in progress_bar:
            yield item