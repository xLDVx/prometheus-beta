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

class HuffmanCodec:
    """A class to manage Huffman encoding and decoding."""
    def __init__(self, data=None):
        """
        Initialize Huffman codec.
        
        Args:
            data (str, optional): Data to encode
        """
        self.original_input = data
        self.freq_dict = self._build_frequency_dict(data) if data else {}
        self.huffman_tree = self._build_huffman_tree() if data else None
        self.codes = self._build_huffman_codes() if data else {}
    
    def _build_frequency_dict(self, data):
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
    
    def _build_huffman_tree(self):
        """
        Construct Huffman tree from frequency dictionary.
        
        Returns:
            HuffmanNode: Root of the Huffman tree
        
        Raises:
            ValueError: If frequency dictionary is empty
        """
        if not self.freq_dict:
            raise ValueError("Frequency dictionary cannot be empty")
        
        # Special case for single character
        if len(self.freq_dict) == 1:
            char, freq = list(self.freq_dict.items())[0]
            root = HuffmanNode(char, freq)
            # If single character, add a dummy node to allow decoding
            root.left = HuffmanNode(char, 1)
            return root
        
        # Create priority queue of nodes
        heap = [HuffmanNode(char, freq) for char, freq in self.freq_dict.items()]
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
    
    def _build_huffman_codes(self):
        """
        Generate Huffman codes from the Huffman tree.
        
        Returns:
            dict: Mapping of characters to their Huffman codes
        """
        if not self.huffman_tree:
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
        
        traverse(self.huffman_tree, '')
        return codes
    
    def encode(self):
        """
        Encode input data using Huffman coding.
        
        Returns:
            tuple: (encoded_data, huffman_tree)
        
        Raises:
            ValueError: If input is empty
        """
        if not self.original_input:
            raise ValueError("Input data cannot be empty")
        
        # Encode the data
        encoded_data = ''.join(self.codes[char] for char in self.original_input)
        
        return encoded_data, self.huffman_tree
    
    def decode(self, encoded_data, huffman_tree):
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
            return huffman_tree.left.char * (len(encoded_data) // len('0'))
        
        decoded_data = []
        current_node = huffman_tree
        
        try:
            for bit in encoded_data:
                # Traverse down the tree based on the bit
                current_node = current_node.left if bit == '0' else current_node.right
                
                # If we've reached a leaf node, we've found a character
                if current_node.char is not None:
                    decoded_data.append(current_node.char)
                    # Reset to root for next character
                    current_node = huffman_tree
        except AttributeError:
            raise ValueError("Invalid Huffman tree or encoded data")
        
        # Ensure we've decoded the entire encoded data
        if current_node != huffman_tree:
            raise ValueError("Invalid encoded data")
        
        return ''.join(decoded_data)

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
    codec = HuffmanCodec(data)
    return codec.encode()