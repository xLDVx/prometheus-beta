def reverse_bits(n: int) -> int:
    """
    Reverse the bits of a given 32-bit unsigned integer.
    
    Args:
        n (int): The input 32-bit unsigned integer to reverse.
    
    Returns:
        int: The integer with its bits reversed.
    
    Raises:
        ValueError: If the input is not a non-negative 32-bit integer.
    
    Examples:
        >>> reverse_bits(43261596)  # 00000010100101000001111010011100 -> 964176192
        964176192
        >>> reverse_bits(4294967295)  # All 1s
        4294967295
        >>> reverse_bits(0)  # All 0s
        0
    """
    # Validate input
    if not isinstance(n, int) or n < 0 or n > 0xFFFFFFFF:
        raise ValueError("Input must be a 32-bit unsigned integer (0-4294967295)")
    
    # Initialize result
    result = 0
    
    # Reverse bits by iterating through all 32 bits
    for i in range(32):
        # Left shift result and add the least significant bit of n
        result = (result << 1) | (n & 1)
        # Right shift n to process next bit
        n >>= 1
    
    return result