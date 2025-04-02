import time
import functools
import logging
from typing import Callable, Any

def log_query_execution_time(logger: logging.Logger = None) -> Callable:
    """
    A decorator to log database query execution times.

    Args:
        logger (logging.Logger, optional): Logger to use for recording execution times. 
                                           If not provided, uses root logger.

    Returns:
        Callable: Decorated function that logs execution time of the query.

    Example:
        >>> import logging
        >>> logging.basicConfig(level=logging.INFO)
        >>> @log_query_execution_time()
        ... def example_query():
        ...     time.sleep(0.1)  # Simulating a database query
        ...     return "Query result"
    """
    def decorator(func: Callable) -> Callable:
        @functools.wraps(func)
        def wrapper(*args: Any, **kwargs: Any) -> Any:
            # Use provided logger or root logger
            log = logger or logging.getLogger()
            
            # Start timing
            start_time = time.time()
            
            try:
                # Execute the function
                result = func(*args, **kwargs)
                
                # Calculate execution time
                execution_time = time.time() - start_time
                
                # Log the execution time
                log.info(f"Query '{func.__name__}' executed in {execution_time:.4f} seconds")
                
                return result
            
            except Exception as e:
                # Log any exceptions that occur during query execution
                log.error(f"Error in query '{func.__name__}': {str(e)}")
                raise
        
        return wrapper
    
    return decorator