import os
import tarfile
from typing import Union, List, Optional

def extract_tar_archive(archive_path: str, 
                        extract_path: Optional[str] = None, 
                        specific_files: Optional[List[str]] = None) -> List[str]:
    """
    Extract files from a tar archive with flexible options.

    Args:
        archive_path (str): Path to the tar archive file.
        extract_path (Optional[str]): Directory to extract files to. 
                                      If None, uses the archive's directory.
        specific_files (Optional[List[str]]): List of specific files to extract. 
                                              If None, extracts all files.

    Returns:
        List[str]: Paths of extracted files.

    Raises:
        FileNotFoundError: If the archive file does not exist.
        tarfile.TarError: If there are issues with the tar file.
        ValueError: If the archive_path is not a tar file.
    """
    # Validate input
    if not os.path.exists(archive_path):
        raise FileNotFoundError(f"Archive file not found: {archive_path}")
    
    if not tarfile.is_tarfile(archive_path):
        raise ValueError(f"Not a valid tar file: {archive_path}")

    # Determine extraction path
    if extract_path is None:
        extract_path = os.path.dirname(os.path.abspath(archive_path)) or '.'
    
    # Ensure extraction directory exists
    os.makedirs(extract_path, exist_ok=True)

    # List to store extracted file paths
    extracted_files = []

    # Open the tar file
    with tarfile.open(archive_path, 'r:*') as tar:
        # If specific files are requested
        if specific_files:
            for file in specific_files:
                try:
                    tar.extract(file, path=extract_path)
                    extracted_files.append(os.path.join(extract_path, file))
                except KeyError:
                    # Skip files not in the archive
                    continue
        else:
            # Extract all files
            tar.extractall(path=extract_path)
            extracted_files = [
                os.path.join(extract_path, name) 
                for name in tar.getnames()
            ]

    return extracted_files