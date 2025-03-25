import lzma
import io

def lzma_compress(data):
    """
    Compress data using LZMA compression algorithm.

    Args:
        data (bytes or str): The input data to compress.
            If str is provided, it will be encoded to UTF-8 bytes.

    Returns:
        bytes: Compressed data in LZMA format.

    Raises:
        TypeError: If input is not bytes or str.
        ValueError: If input is empty.
    """
    # Validate input
    if not data:
        raise ValueError("Input data cannot be empty")

    # Convert to bytes if input is string
    if isinstance(data, str):
        data = data.encode('utf-8')
    
    # Ensure input is bytes
    if not isinstance(data, bytes):
        raise TypeError("Input must be bytes or str")

    try:
        # Compress the data
        return lzma.compress(data, preset=9)
    
    except Exception as e:
        raise RuntimeError(f"LZMA compression failed: {str(e)}")

def lzma_decompress(compressed_data):
    """
    Decompress LZMA compressed data.

    Args:
        compressed_data (bytes): LZMA compressed data to decompress.

    Returns:
        bytes: Decompressed data.

    Raises:
        TypeError: If input is not bytes.
        ValueError: If input is empty.
        RuntimeError: If decompression fails.
    """
    # Validate input
    if not compressed_data:
        raise ValueError("Compressed data cannot be empty")

    if not isinstance(compressed_data, bytes):
        raise TypeError("Compressed data must be bytes")

    try:
        # Decompress the data
        return lzma.decompress(compressed_data)
    
    except Exception as e:
        raise RuntimeError(f"LZMA decompression failed: {str(e)}")