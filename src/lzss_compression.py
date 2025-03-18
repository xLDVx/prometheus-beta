"""
LZSS (Lempel-Ziv-Storer-Szymanski) Compression Algorithm Implementation.

This module provides functions for LZSS compression and decompression.
LZSS is a dictionary coding compression algorithm that replaces repeated 
occurrences of data with references to a single copy of that data.
"""

class LZSSCompressor:
    def __init__(self, window_size=4096, min_match_length=3):
        """
        Initialize the LZSS Compressor.
        
        Args:
            window_size (int): Size of the sliding window for searching matches. 
                               Default is 4096.
            min_match_length (int): Minimum length of a match to be encoded. 
                                    Default is 3.
        """
        self.window_size = window_size
        self.min_match_length = min_match_length

    def compress(self, data):
        """
        Compress the input data using LZSS algorithm.
        
        Args:
            data (bytes or str): Input data to compress.
        
        Returns:
            bytes: Compressed data.
        
        Raises:
            TypeError: If input is not bytes or convertible to bytes.
            ValueError: If input is empty.
        """
        # Ensure input is bytes
        if isinstance(data, str):
            data = data.encode('utf-8')
        
        if not data:
            raise ValueError("Input data cannot be empty")
        
        # Convert to list for easier manipulation
        data = list(data)
        compressed = []
        
        # Initialize search window
        current_pos = 0
        while current_pos < len(data):
            # Find the longest match in the window
            match_length = 0
            match_pos = 0
            
            # Define search window range
            start = max(0, current_pos - self.window_size)
            
            # Search for the longest match
            for j in range(start, current_pos):
                # Check potential match length
                potential_match_length = 0
                while (current_pos + potential_match_length < len(data) and 
                       potential_match_length < 15 and  # Limit match length to 4 bits
                       data[j + potential_match_length] == data[current_pos + potential_match_length]):
                    potential_match_length += 1
                
                # Update best match if longer
                if potential_match_length > match_length:
                    match_length = potential_match_length
                    match_pos = current_pos - j
            
            # Decide whether to encode a match or a literal
            if match_length >= self.min_match_length:
                # Encode match: (offset, length)
                # Use 12 bits for offset, 4 bits for length
                compressed.extend([
                    0,  # Match flag
                    ((match_pos & 0xF00) >> 8) | ((match_length - self.min_match_length) & 0x0F),
                    match_pos & 0xFF
                ])
                current_pos += match_length
            else:
                # Encode literal
                compressed.extend([1, data[current_pos]])  # Literal flag and value
                current_pos += 1
        
        return bytes(compressed)

    def decompress(self, compressed_data):
        """
        Decompress LZSS compressed data.
        
        Args:
            compressed_data (bytes): Compressed input data.
        
        Returns:
            bytes: Decompressed data.
        
        Raises:
            TypeError: If input is not bytes.
            ValueError: If input is empty or malformed.
        """
        # Ensure input is bytes
        if not isinstance(compressed_data, bytes):
            raise TypeError("Input must be bytes")
        
        if not compressed_data:
            raise ValueError("Compressed data cannot be empty")
        
        # Convert to list for easier manipulation
        compressed_data = list(compressed_data)
        decompressed = []
        
        i = 0
        while i < len(compressed_data):
            if i + 1 >= len(compressed_data):
                raise ValueError("Malformed compressed data")
            
            flag = compressed_data[i]
            
            if flag == 0:  # Match
                if i + 2 >= len(compressed_data):
                    raise ValueError("Malformed compressed data")
                
                # Extract offset and length
                match_info = compressed_data[i+1]
                offset_high = (match_info & 0xF0) << 4
                length = (match_info & 0x0F) + self.min_match_length
                offset_low = compressed_data[i+2]
                offset = offset_high | offset_low
                
                # Reconstruct matched sequence
                start = len(decompressed) - offset
                for j in range(length):
                    if start + j < 0:
                        raise ValueError("Invalid offset in compressed data")
                    decompressed.append(decompressed[start + j])
                
                i += 3
            elif flag == 1:  # Literal
                if i + 1 >= len(compressed_data):
                    raise ValueError("Malformed compressed data")
                decompressed.append(compressed_data[i+1])
                i += 2
            else:
                # Adjust for unexpected flags
                i += 1