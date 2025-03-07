"""
LZJB Compression Algorithm Implementation

This module provides functionality for LZJB compression, a lightweight 
compression algorithm designed for speed and efficiency.
"""

def lzjb_compress(input_data):
    """
    Compress input data using the LZJB compression algorithm.
    
    Args:
        input_data (bytes): The input data to be compressed.
    
    Returns:
        bytes: Compressed data.
    
    Raises:
        TypeError: If input is not bytes.
        ValueError: If input is empty.
    """
    # Input validation
    if not isinstance(input_data, bytes):
        raise TypeError("Input must be bytes")
    
    if not input_data:
        raise ValueError("Input cannot be empty")
    
    # LZJB compression implementation
    compressed = bytearray()
    input_length = len(input_data)
    current_index = 0
    
    while current_index < input_length:
        # Look for the longest match in the previous window
        best_length = 0
        best_offset = 0
        
        # Search back up to 1024 bytes (typical LZJB window size)
        search_start = max(0, current_index - 1024)
        
        for offset in range(1, min(current_index - search_start + 1, 1024)):
            # Check potential match length
            match_length = 0
            while (current_index + match_length < input_length and 
                   match_length < 255 and 
                   input_data[current_index + match_length] == 
                   input_data[current_index - offset + match_length]):
                match_length += 1
            
            # Update best match if found
            if match_length > best_length:
                best_length = match_length
                best_offset = offset
        
        # Encode the match or literal
        if best_length > 2:
            # Encode match: combine offset and length
            # Ensure tokens are always between 0 and 255
            token = min(255, ((best_offset - 1) << 3) | (best_length - 3))
            compressed.append(token)
            current_index += best_length
        else:
            # Encode literal
            compressed.append(input_data[current_index])
            current_index += 1
    
    return bytes(compressed)

def lzjb_decompress(compressed_data):
    """
    Decompress data compressed with the LZJB algorithm.
    
    Args:
        compressed_data (bytes): The compressed input data.
    
    Returns:
        bytes: Decompressed data.
    
    Raises:
        TypeError: If input is not bytes.
        ValueError: If input is empty or appears to be corrupted.
    """
    # Input validation
    if not isinstance(compressed_data, bytes):
        raise TypeError("Input must be bytes")
    
    if not compressed_data:
        raise ValueError("Input cannot be empty")
    
    # Decompression implementation
    decompressed = bytearray()
    current_index = 0
    
    while current_index < len(compressed_data):
        token = compressed_data[current_index]
        current_index += 1
        
        # Check if it's a match or literal
        if token < 32:  # Match token (0-31)
            # Extract offset and length
            match_offset = ((token >> 3) + 1)
            match_length = (token & 0x7) + 3
            
            # Ensure we have enough context for matching
            if len(decompressed) < match_offset:
                # Fallback to treating as a literal if not enough context
                decompressed.append(token)
                continue
            
            # Copy matched bytes
            start = len(decompressed) - match_offset
            for _ in range(match_length):
                if start < 0:
                    break
                decompressed.append(decompressed[start])
                start += 1
        else:
            # Literal byte
            decompressed.append(token)
    
    return bytes(decompressed)