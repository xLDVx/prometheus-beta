"""
Arithmetic Coding Implementation for Data Compression

This module provides functions for implementing arithmetic coding,
a data compression technique that encodes entire messages into a single number.
"""

from collections import Counter
from typing import List, Union, Dict


def arithmetic_encode(data: Union[str, List[str]]) -> Dict[str, Union[float, Dict[str, float]]]:
    """
    Perform arithmetic encoding on the input data.
    
    Args:
        data (Union[str, List[str]]): Input data to be compressed
    
    Returns:
        Dict[str, Union[float, Dict[str, float]]]: A dictionary containing:
            - 'compressed_value': The final compressed value (float)
            - 'probabilities': Probability distribution of symbols
    
    Raises:
        ValueError: If input data is empty
    """
    # Validate input
    if not data:
        raise ValueError("Input data cannot be empty")
    
    # Convert input to list of characters if it's a string
    if isinstance(data, str):
        data = list(data)
    
    # Calculate symbol probabilities
    symbol_counts = Counter(data)
    total_symbols = len(data)
    
    # Calculate cumulative probabilities
    probabilities = {}
    cumulative_prob = 0.0
    for symbol, count in symbol_counts.items():
        prob = count / total_symbols
        probabilities[symbol] = {
            'frequency': count,
            'probability': prob,
            'low': cumulative_prob,
            'high': cumulative_prob + prob
        }
        cumulative_prob += prob
    
    # Initial range
    low = 0.0
    high = 1.0
    
    # Encode each symbol
    for symbol in data:
        # Calculate range size
        range_size = high - low
        
        # Update range based on symbol probabilities
        symbol_info = probabilities[symbol]
        high = low + range_size * symbol_info['high']
        low = low + range_size * symbol_info['low']
    
    # The final compressed value is the midpoint of the final range
    compressed_value = (low + high) / 2
    
    return {
        'compressed_value': compressed_value,
        'probabilities': probabilities
    }


def arithmetic_decode(compressed_value: float, probabilities: Dict[str, Dict[str, float]], 
                      length: int) -> str:
    """
    Decode a compressed value back to the original data.
    
    Args:
        compressed_value (float): The compressed value
        probabilities (Dict): Probability distribution of symbols
        length (int): Original length of the data
    
    Returns:
        str: Decoded data
    
    Raises:
        ValueError: If inputs are invalid
    """
    # Validate inputs
    if not probabilities or length <= 0:
        raise ValueError("Invalid inputs for decoding")
    
    # Sort symbols by their low probability bounds
    sorted_symbols = sorted(probabilities.keys(), 
                             key=lambda x: probabilities[x]['low'])
    
    # Decoded data will be stored here
    decoded_data = []
    
    # Current working value
    current = compressed_value
    
    # Decode each symbol
    for _ in range(length):
        # Find the symbol that contains the current value
        for symbol in sorted_symbols:
            sym_prob = probabilities[symbol]
            if sym_prob['low'] <= current < sym_prob['high']:
                decoded_data.append(symbol)
                
                # Adjust current value relative to the symbol's range
                current = (current - sym_prob['low']) / (sym_prob['high'] - sym_prob['low'])
                break
    
    return ''.join(decoded_data)