"""
LZ4 Compression Algorithm Implementation

This module provides a basic implementation of the LZ4 compression algorithm.
LZ4 is a lossless compression algorithm that focuses on compression and 
decompression speed.

Note: This is a simplified implementation and not a full production-ready LZ4 codec.
"""

def lz4_compress(data):
    """
    Compress input data using a simplified LZ4-like compression algorithm.
    
    Args:
        data (bytes or str): Input data to be compressed
    
    Returns:
        bytes: Compressed data
    
    Raises:
        TypeError: If input is not bytes or str
        ValueError: If input is empty
    """
    # Validate input
    if not data:
        raise ValueError("Input data cannot be empty")
    
    # Convert to bytes if input is a string
    if isinstance(data, str):
        data = data.encode('utf-8')
    
    if not isinstance(data, bytes):
        raise TypeError("Input must be bytes or str")
    
    # Compression variables
    compressed = bytearray()
    i = 0
    
    while i < len(data):
        # Find matches
        best_match_length = 0
        best_match_offset = 0
        
        # Search backward for longest match
        for j in range(max(0, i - 65535), i):
            current_match_length = 0
            
            # Check how long the match continues
            while (i + current_match_length < len(data) and 
                   current_match_length < 255 and 
                   data[j + current_match_length] == data[i + current_match_length]):
                current_match_length += 1
            
            # Update best match if longer
            if current_match_length > best_match_length:
                best_match_length = current_match_length
                best_match_offset = i - j
        
        # If no good match found, store literal
        if best_match_length < 4:
            # Append literal byte
            compressed.append(1)  # Literal length
            compressed.append(data[i])
            i += 1
        else:
            # Store literals before the match
            compressed.append(best_match_length)  # Token with match length
            compressed.extend(best_match_offset.to_bytes(2, byteorder='little'))  # Offset
            i += best_match_length
    
    return bytes(compressed)

def lz4_decompress(compressed_data):
    """
    Decompress data compressed with the simplified LZ4-like algorithm.
    
    Args:
        compressed_data (bytes): Compressed input data
    
    Returns:
        bytes: Decompressed data
    
    Raises:
        TypeError: If input is not bytes
        ValueError: If input is empty or compressed data is invalid
    """
    # Validate input
    if not compressed_data:
        raise ValueError("Compressed data cannot be empty")
    
    if not isinstance(compressed_data, bytes):
        raise TypeError("Compressed data must be bytes")
    
    # Decompression variables
    decompressed = bytearray()
    i = 0
    
    while i < len(compressed_data):
        # Get token: can be either literal length or match length
        token = compressed_data[i]
        
        # Literal mode
        if token == 1:
            # Single literal byte
            decompressed.append(compressed_data[i+1])
            i += 2
            continue
        
        # Match mode
        match_length = token
        match_offset = int.from_bytes(compressed_data[i+1:i+3], byteorder='little')
        
        # Reconstruct matched sequence
        start = len(decompressed) - match_offset
        
        for j in range(match_length):
            if start + j < 0 or start + j >= len(decompressed):
                break
            decompressed.append(decompressed[start + j])
        
        i += 3
    
    return bytes(decompressed)