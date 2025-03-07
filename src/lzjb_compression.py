"""
LZJB Compression Algorithm Implementation

This module provides functionality for LZJB-inspired compression.
"""

def lzjb_compress(input_data):
    """
    Compress input data using a LZJB-inspired algorithm.
    
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
    
    # Compression implementation
    compressed = bytearray()
    input_length = len(input_data)
    current_index = 0
    
    while current_index < input_length:
        # Search window (look back limited distance)
        window_start = max(0, current_index - 1024)
        window = input_data[window_start:current_index]
        
        # Find longest match
        best_length = 0
        best_offset = 0
        
        for offset in range(1, min(current_index - window_start + 1, 1024)):
            # Start matching
            match_length = 0
            max_match = min(255, input_length - current_index)
            
            while (match_length < max_match and 
                   input_data[current_index + match_length] == 
                   input_data[current_index - offset + match_length]):
                match_length += 1
            
            # Update best match
            if match_length > best_length:
                best_length = match_length
                best_offset = offset
        
        # Encoding decision
        if best_length > 2:
            # Encode match (packed token)
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
    Decompress data compressed with the LZJB-inspired algorithm.
    
    Args:
        compressed_data (bytes): The compressed input data.
    
    Returns:
        bytes: Decompressed data.
    
    Raises:
        TypeError: If input is not bytes.
        ValueError: If input is empty.
    """
    # Input validation
    if not isinstance(compressed_data, bytes):
        raise TypeError("Input must be bytes")
    
    if not compressed_data:
        raise ValueError("Input cannot be empty")
    
    # Decompression implementation
    decompressed = bytearray()
    
    i = 0
    while i < len(compressed_data):
        token = compressed_data[i]
        i += 1
        
        if token < 32:  # Match token
            # Extract offset and length
            match_offset = ((token >> 3) + 1)
            match_length = (token & 0x7) + 3
            
            # Validate context
            if len(decompressed) < match_offset:
                # Fallback: treat as literal
                decompressed.append(token)
                continue
            
            # Reconstruct match
            start_pos = len(decompressed) - match_offset
            for _ in range(match_length):
                if start_pos < 0:
                    break
                decompressed.append(decompressed[start_pos])
                start_pos += 1
        else:
            # Literal byte
            decompressed.append(token)
    
    return bytes(decompressed)