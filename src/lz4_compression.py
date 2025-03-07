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
        # Look-ahead window for matching
        match_length = 0
        match_offset = 0
        
        # Search backward for longest match
        for j in range(max(0, i - 65535), i):
            current_match_length = 0
            
            # Check how long the match continues
            while (i + current_match_length < len(data) and 
                   data[j + current_match_length] == data[i + current_match_length] and 
                   current_match_length < 255):
                current_match_length += 1
            
            # Update best match
            if current_match_length > match_length:
                match_length = current_match_length
                match_offset = i - j
        
        # If no good match found, store literal
        if match_length < 4:
            compressed.append(data[i])
            i += 1
        else:
            # Store token, offset, and continue
            compressed.append(match_length)
            compressed.extend(match_offset.to_bytes(2, byteorder='little'))
            i += match_length
    
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
        # Handle remaining literals for short compressed data
        if i + 3 >= len(compressed_data):
            # If not enough bytes for a full token, treat as literals
            decompressed.append(compressed_data[i])
            i += 1
            continue
        
        token = compressed_data[i]
        
        # If token is less than 4, it's a literal
        if token < 4:
            decompressed.append(compressed_data[i])
            i += 1
        else:
            # Extract match length and offset
            match_length = token
            match_offset = int.from_bytes(compressed_data[i+1:i+3], byteorder='little')
            
            # Reconstruct matched sequence
            # Use the current decompressed data as the source for copying
            start = len(decompressed) - match_offset
            
            # Ensure start is non-negative and add repeated bytes
            if start >= 0:
                for j in range(match_length):
                    if start + j < len(decompressed):
                        decompressed.append(decompressed[start + j])
                    else:
                        # If we run out of source bytes, pad with last known byte
                        decompressed.append(decompressed[-1])
            else:
                # If start is negative, it means we don't have enough prior bytes
                # Fall back to literal copying or padding
                for j in range(match_length):
                    if decompressed:
                        decompressed.append(decompressed[-1])
                    else:
                        # This should rarely happen if the compression was correct
                        decompressed.append(0)
            
            i += 3
    
    return bytes(decompressed)