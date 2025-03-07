"""
LZJB-Inspired Compression Algorithm Implementation

This module provides a simplified compression algorithm 
inspired by the principles of LZJB compression.
"""

def lzjb_compress(input_data):
    """
    Compress input data using a simplified LZJB-inspired algorithm.
    
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
    
    # Compression parameters
    MAX_OFFSET = 1024
    MAX_LENGTH = 255
    
    # Compression implementation
    compressed = bytearray()
    input_length = len(input_data)
    current_index = 0
    
    while current_index < input_length:
        # Define search window
        window_start = max(0, current_index - MAX_OFFSET)
        
        # Find longest match
        match_length = 0
        match_offset = 0
        
        # Check for repeated sequences
        for offset in range(1, min(current_index - window_start + 1, MAX_OFFSET)):
            # Try to match subsequent bytes
            current_match_length = 0
            while (current_index + current_match_length < input_length and
                   current_match_length < MAX_LENGTH and
                   input_data[current_index + current_match_length] == 
                   input_data[current_index - offset + current_match_length]):
                current_match_length += 1
            
            # Update best match
            if current_match_length > match_length:
                match_length = current_match_length
                match_offset = offset
        
        # Encode match or literal
        if match_length > 2:
            # Encode match with packed token
            # Shift offset and combine with length
            token = ((match_offset - 1) << 3) | (match_length - 3)
            compressed.append(min(255, token))
            current_index += match_length
        else:
            # Special handling for repeated single character
            current_char = input_data[current_index]
            repeat_count = 1
            
            # Look ahead for repeated character
            while (current_index + repeat_count < input_length and 
                   repeat_count < MAX_LENGTH and
                   input_data[current_index + repeat_count] == current_char):
                repeat_count += 1
            
            if repeat_count > 2:
                # Use a special token for repeated character
                token = ((0 - 1) << 3) | (repeat_count - 3)
                compressed.append(min(255, token))
                compressed.append(current_char)
                current_index += repeat_count
            else:
                # Encode literal
                compressed.append(current_char)
                current_index += 1
    
    return bytes(compressed)

def lzjb_decompress(compressed_data):
    """
    Decompress data compressed with the simplified LZJB-inspired algorithm.
    
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
    current_index = 0
    
    while current_index < len(compressed_data):
        token = compressed_data[current_index]
        current_index += 1
        
        if token < 32:  # Match or repeat token (0-31)
            # Check if it's a special repeated character case
            if token == 0:
                # Next byte is repeated character
                if current_index >= len(compressed_data):
                    break
                repeat_char = compressed_data[current_index]
                current_index += 1
                repeat_length = (token & 0x7) + 3
                decompressed.extend([repeat_char] * repeat_length)
            else:
                # Extract offset and length
                match_offset = ((token >> 3) + 1)
                match_length = (token & 0x7) + 3
                
                # Reconstruct match
                if len(decompressed) < match_offset:
                    # Not enough context, treat as literal
                    decompressed.append(token)
                    continue
                
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