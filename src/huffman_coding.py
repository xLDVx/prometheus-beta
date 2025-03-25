from collections import Counter, defaultdict
import heapq

class HuffmanNode:
    """Represents a node in the Huffman tree."""
    def __init__(self, char, freq):
        self.char = char
        self.freq = freq
        self.left = None
        self.right = None
    
    def __lt__(self, other):
        """Allow comparison for heapq sorting."""
        return self.freq < other.freq

def build_frequency_dict(data):
    """
    Build a frequency dictionary for input data.
    
    Args:
        data (str): Input string to analyze
    
    Returns:
        dict: Character frequency dictionary
    """
    if not data:
        return {}
    return dict(Counter(data))

def build_huffman_tree(freq_dict):
    """
    Construct Huffman tree from frequency dictionary.
    
    Args:
        freq_dict (dict): Character frequency dictionary
    
    Returns:
        HuffmanNode: Root of the Huffman tree
    
    Raises:
        ValueError: If frequency dictionary is empty
    """
    if not freq_dict:
        raise ValueError("Frequency dictionary cannot be empty")
    
    # Special case for single character
    if len(freq_dict) == 1:
        char, freq = list(freq_dict.items())[0]
        root = HuffmanNode(char, freq)
        # If single character, add a dummy node to allow decoding
        root.left = HuffmanNode(char, 1)
        return root
    
    # Create priority queue of nodes
    heap = [HuffmanNode(char, freq) for char, freq in freq_dict.items()]
    heapq.heapify(heap)
    
    # Build tree by combining nodes
    while len(heap) > 1:
        left = heapq.heappop(heap)
        right = heapq.heappop(heap)
        
        # Create internal node with combined frequency
        internal = HuffmanNode(None, left.freq + right.freq)
        internal.left = left
        internal.right = right
        
        heapq.heappush(heap, internal)
    
    return heap[0]

def build_huffman_codes(root):
    """
    Generate Huffman codes from the Huffman tree.
    
    Args:
        root (HuffmanNode): Root of the Huffman tree
    
    Returns:
        dict: Mapping of characters to their Huffman codes
    """
    if not root:
        return {}
    
    codes = {}
    
    def traverse(node, current_code):
        """Recursive helper to generate codes."""
        if not node:
            return
        
        # Leaf node (has a character)
        if node.char is not None:
            # Special case for single character 
            codes[node.char] = current_code if current_code else '0'
            return
        
        # Traverse left with '0'
        if node.left:
            traverse(node.left, current_code + '0')
        
        # Traverse right with '1'
        if node.right:
            traverse(node.right, current_code + '1')
    
    traverse(root, '')
    return codes

def huffman_encode(data):
    """
    Encode input data using Huffman coding.
    
    Args:
        data (str): Input string to encode
    
    Returns:
        tuple: (encoded_data, huffman_tree)
    
    Raises:
        ValueError: If input is empty
    """
    if not data:
        raise ValueError("Input data cannot be empty")
    
    # Handle single character case
    if len(set(data)) == 1:
        return '0' * len(data), build_huffman_tree({data[0]: len(data)})
    
    # Build frequency dictionary
    freq_dict = build_frequency_dict(data)
    
    # Build Huffman tree
    huffman_tree = build_huffman_tree(freq_dict)
    
    # Generate Huffman codes
    huffman_codes = build_huffman_codes(huffman_tree)
    
    # Encode the data
    encoded_data = ''.join(huffman_codes[char] for char in data)
    
    return encoded_data, huffman_tree

def huffman_decode(encoded_data, huffman_tree):
    """
    Decode Huffman encoded data.
    
    Args:
        encoded_data (str): Encoded binary string
        huffman_tree (HuffmanNode): Huffman tree used for encoding
    
    Returns:
        str: Decoded original data
    
    Raises:
        ValueError: If encoded data or Huffman tree is invalid
    """
    # Handle None cases
    if huffman_tree is None:
        raise ValueError("Huffman tree cannot be None")
    
    # Empty input
    if not encoded_data:
        return ""
    
    # Special case for single character
    if hasattr(huffman_tree, 'left') and huffman_tree.left and huffman_tree.left.char is not None:
        return huffman_tree.left.char * len(encoded_data)
    
    decoded_data = []
    current_node = huffman_tree
    
    try:
        # First, verify that the encoded data can be fully decoded
        test_data = encoded_data
        verify_node = huffman_tree
        verify_decoded = []
        
        while test_data:
            verify_node = huffman_tree
            for bit in test_data:
                verify_node = verify_node.left if bit == '0' else verify_node.right
                
                if verify_node.char is not None:
                    verify_decoded.append(verify_node.char)
                    test_data = test_data[len(verify_node.char):]
                    break
            else:
                raise ValueError("Cannot fully decode the data")
        
        # If verification passes, do the actual decoding
        for bit in encoded_data:
            # Traverse down the tree based on the bit
            current_node = current_node.left if bit == '0' else current_node.right
            
            # If we've reached a leaf node, we've found a character
            if current_node.char is not None:
                decoded_data.append(current_node.char)
                # Reset to root for next character
                current_node = huffman_tree
    except (AttributeError, ValueError):
        raise ValueError("Invalid Huffman tree or encoded data")
    
    # Ensure we've decoded the entire encoded data
    if current_node != huffman_tree:
        raise ValueError("Invalid encoded data")
    
    return ''.join(verify_decoded)