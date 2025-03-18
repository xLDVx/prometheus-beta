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
        
        data = list(data)
        compressed = []
        current_pos = 0
        
        while current_pos < len(data):
            # Find the longest match
            best_match_length = 0
            best_match_pos = 0
            
            # Search window starts from the maximum possible lookback
            start = max(0, current_pos - self.window_size)
            
            for j in range(start, current_pos):
                # Check match length starting from this position
                match_length = 0
                while (current_pos + match_length < len(data) and 
                       match_length < 15 and  # 4-bit length encoding
                       data[j + match_length] == data[current_pos + match_length]):
                    match_length += 1
                
                # Update best match
                if match_length > best_match_length:
                    best_match_length = match_length
                    best_match_pos = current_pos - j
            
            # Encode match or literal
            if best_match_length >= self.min_match_length:
                # Encode match (flag=0, offset high + length, offset low)
                encoded_length = best_match_length - self.min_match_length
                encoded_offset_high = (best_match_pos >> 8) & 0x0F
                encoded_offset_low = best_match_pos & 0xFF
                
                compressed.extend([
                    0,  # Match flag
                    (encoded_offset_high << 4) | encoded_length,
                    encoded_offset_low
                ])
                current_pos += best_match_length
            else:
                # Literal (flag=1, value)
                compressed.extend([1, data[current_pos]])
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
        if not isinstance(compressed_data, bytes):
            raise TypeError("Input must be bytes")
        
        if not compressed_data:
            raise ValueError("Compressed data cannot be empty")
        
        compressed_data = list(compressed_data)
        decompressed = []
        i = 0
        
        while i < len(compressed_data):
            # Ensure we have enough data to process
            if i + 1 >= len(compressed_data):
                break
            
            # Get flag and next data
            flag = compressed_data[i]
            
            if flag == 0:  # Match
                # Check we have enough data for match decoding
                if i + 2 >= len(compressed_data):
                    break
                
                # Decode offset and length
                match_info = compressed_data[i+1]
                length = (match_info & 0x0F) + self.min_match_length
                offset_high = (match_info & 0xF0) >> 4
                offset_low = compressed_data[i+2]
                offset = (offset_high << 8) | offset_low
                
                # Reconstruct matched sequence
                start = len(decompressed) - offset
                for j in range(length):
                    if start + j < 0:
                        break
                    decompressed.append(decompressed[start + j])
                
                i += 3
            elif flag == 1:  # Literal
                # Ensure we have a literal value
                if i + 1 >= len(compressed_data):
                    break
                
                decompressed.append(compressed_data[i+1])
                i += 2
            else:
                # Skip unexpected flags
                i += 1
        
        return bytes(decompressed)