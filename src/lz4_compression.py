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
        # Literal bytes
        start_i = i
        
        # Look for repeated sequences
        while i < len(data) and i - start_i < 255:
            # Try to find a match at most 65535 bytes back
            match_found = False
            for j in range(max(0, start_i - 65535), start_i):
                match_length = 0
                while (i + match_length < len(data) and 
                       data[j + match_length] == data[i + match_length] and 
                       match_length < 255):
                    match_length += 1
                
                # Long enough match found
                if match_length > 3:
                    # If we've stored some literals, do so
                    lit_len = start_i - i
                    if lit_len > 0:
                        compressed.append(lit_len)
                        compressed.extend(data[i:start_i])
                    
                    # Store match token
                    compressed.append(match_length)
                    compressed.extend((start_i - j).to_bytes(2, byteorder='little'))
                    
                    # Advance pointers
                    i = start_i + match_length
                    match_found = True
                    break
                
            # No match or too short match
            if not match_found:
                i += 1
        
        # Store remaining literals if any
        if i > start_i:
            lit_len = i - start_i
            compressed.append(lit_len)
            compressed.extend(data[start_i:i])
    
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
        # Extract literal length
        lit_len = compressed_data[i]
        i += 1
        
        # Copy literals
        if lit_len > 0:
            if i + lit_len > len(compressed_data):
                raise ValueError("Invalid compressed data: not enough literals")
            decompressed.extend(compressed_data[i:i+lit_len])
            i += lit_len
        
        # Check if we've reached the end
        if i >= len(compressed_data):
            break
        
        # Extract match token and offset
        match_len = compressed_data[i]
        match_offset = int.from_bytes(compressed_data[i+1:i+3], byteorder='little')
        i += 3
        
        # Reconstruct matched sequence
        start = len(decompressed) - match_offset
        if start < 0:
            raise ValueError("Invalid compressed data: back-reference out of bounds")
        
        for j in range(match_len):
            if start + j >= len(decompressed):
                break
            decompressed.append(decompressed[start + j])
    
    return bytes(decompressed)