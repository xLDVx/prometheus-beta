import os
import typing

def split_file(file_path: str, chunk_size: int, output_dir: typing.Optional[str] = None) -> typing.List[str]:
    """
    Split a large file into smaller chunks.

    Args:
        file_path (str): Path to the input file to be split.
        chunk_size (int): Size of each chunk in bytes.
        output_dir (str, optional): Directory to save chunk files. 
                                    Defaults to same directory as input file.

    Returns:
        List[str]: Paths to the generated chunk files.

    Raises:
        ValueError: If chunk_size is less than or equal to 0.
        FileNotFoundError: If the input file does not exist.
        IOError: If there are issues reading or writing files.
    """
    # Validate inputs
    if chunk_size <= 0:
        raise ValueError("Chunk size must be a positive integer")
    
    # Normalize and validate file path
    file_path = os.path.abspath(file_path)
    if not os.path.exists(file_path):
        raise FileNotFoundError(f"Input file not found: {file_path}")
    
    # Determine output directory
    if output_dir is None:
        output_dir = os.path.dirname(file_path)
    else:
        os.makedirs(output_dir, exist_ok=True)
    
    # Generate base output filename
    base_filename = os.path.basename(file_path)
    
    # List to store chunk file paths
    chunk_files = []
    
    try:
        # Open the input file
        with open(file_path, 'rb') as input_file:
            chunk_num = 1
            while True:
                # Read chunk
                chunk = input_file.read(chunk_size)
                
                # Break if no more data
                if not chunk:
                    break
                
                # Create chunk filename
                chunk_filename = os.path.join(
                    output_dir, 
                    f"{base_filename}.part{chunk_num:03d}"
                )
                
                # Write chunk to file
                with open(chunk_filename, 'wb') as chunk_file:
                    chunk_file.write(chunk)
                
                # Add to list of chunk files
                chunk_files.append(chunk_filename)
                
                # Increment chunk number
                chunk_num += 1
        
        return chunk_files
    
    except IOError as e:
        raise IOError(f"Error processing file: {e}")