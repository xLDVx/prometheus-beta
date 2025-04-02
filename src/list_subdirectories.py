import os
from typing import List

def list_subdirectories(directory_path: str) -> List[str]:
    """
    List all subdirectories in the given directory.

    Args:
        directory_path (str): The path to the directory to search for subdirectories.

    Returns:
        List[str]: A list of subdirectory names (not full paths).

    Raises:
        FileNotFoundError: If the specified directory does not exist.
        NotADirectoryError: If the specified path is not a directory.
        PermissionError: If there are insufficient permissions to access the directory.
    """
    # Validate input
    if not os.path.exists(directory_path):
        raise FileNotFoundError(f"The directory {directory_path} does not exist.")
    
    if not os.path.isdir(directory_path):
        raise NotADirectoryError(f"The path {directory_path} is not a directory.")
    
    # List and filter subdirectories
    try:
        # Use os.scandir for efficient directory iteration
        subdirs = [
            entry.name 
            for entry in os.scandir(directory_path) 
            if entry.is_dir()
        ]
        return sorted(subdirs)
    except PermissionError:
        raise PermissionError(f"Insufficient permissions to access directory {directory_path}")