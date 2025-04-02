def lzc_compress(data):
    """
    Implement Lempel-Ziv-Coffman (LZC) compression algorithm.
    
    Args:
        data (bytes or bytearray): Input data to compress
    
    Returns:
        list: Compressed representation of the input data
    
    Raises:
        TypeError: If input is not bytes or bytearray
        ValueError: If input is empty
    """
    # Input validation
    if not isinstance(data, (bytes, bytearray)):
        raise TypeError("Input must be bytes or bytearray")
    
    if not data:
        raise ValueError("Input data cannot be empty")
    
    # Initialize dictionary and compression output
    dictionary = {bytes([i]): i for i in range(256)}
    next_code = 256
    current_sequence = bytes()
    compressed = []
    
    # Compression algorithm
    for byte in data:
        # Extend current sequence
        candidate = current_sequence + bytes([byte])
        
        # If candidate is in dictionary, continue building sequence
        if candidate in dictionary:
            current_sequence = candidate
        else:
            # Output code for current sequence
            compressed.append(dictionary[current_sequence])
            
            # Add new sequence to dictionary if not full
            if next_code < 65536:  # Limit dictionary size
                dictionary[candidate] = next_code
                next_code += 1
            
            # Reset current sequence to current byte
            current_sequence = bytes([byte])
    
    # Output last sequence
    if current_sequence:
        compressed.append(dictionary[current_sequence])
    
    return compressed

def lzc_decompress(compressed):
    """
    Decompress data compressed with LZC algorithm.
    
    Args:
        compressed (list): Compressed data representation
    
    Returns:
        bytearray: Decompressed data
    
    Raises:
        TypeError: If input is not a list
        ValueError: If input is empty
    """
    # Input validation
    if not isinstance(compressed, list):
        raise TypeError("Input must be a list of integer codes")
    
    if not compressed:
        raise ValueError("Compressed data cannot be empty")
    
    # Initialize dictionary and decompression output
    dictionary = {i: bytes([i]) for i in range(256)}
    next_code = 256
    result = bytearray()
    
    # First code is always added directly
    current_code = compressed[0]
    result.extend(dictionary[current_code])
    
    # Decompression algorithm
    for code in compressed[1:]:
        if code in dictionary:
            # Known code: retrieve and add to result
            decoded = dictionary[code]
        elif code == next_code:
            # Special case: new code not yet in dictionary
            decoded = dictionary[current_code] + bytes([dictionary[current_code][0]])
        else:
            raise ValueError(f"Invalid compressed code: {code}")
        
        result.extend(decoded)
        
        # Add new dictionary entry if not full
        if next_code < 65536:
            new_entry = dictionary[current_code] + bytes([decoded[0]])
            dictionary[next_code] = new_entry
            next_code += 1
        
        current_code = code
    
    return result