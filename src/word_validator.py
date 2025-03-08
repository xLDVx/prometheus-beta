class Queue:
    """
    A simple Queue implementation using a list.
    
    This Queue class provides basic queue operations like enqueue, dequeue, 
    peek, and checking if the queue is empty.
    """
    def __init__(self):
        """
        Initialize an empty queue.
        """
        self._items = []
    
    def enqueue(self, item):
        """
        Add an item to the end of the queue.
        
        Args:
            item: The item to be added to the queue.
        """
        self._items.append(item)
    
    def dequeue(self):
        """
        Remove and return the first item from the queue.
        
        Returns:
            The first item in the queue.
        
        Raises:
            IndexError: If the queue is empty.
        """
        if self.is_empty():
            raise IndexError("Cannot dequeue from an empty queue")
        return self._items.pop(0)
    
    def peek(self):
        """
        Return the first item in the queue without removing it.
        
        Returns:
            The first item in the queue.
        
        Raises:
            IndexError: If the queue is empty.
        """
        if self.is_empty():
            raise IndexError("Cannot peek an empty queue")
        return self._items[0]
    
    def is_empty(self):
        """
        Check if the queue is empty.
        
        Returns:
            bool: True if the queue is empty, False otherwise.
        """
        return len(self._items) == 0
    
    def size(self):
        """
        Get the number of items in the queue.
        
        Returns:
            int: The number of items in the queue.
        """
        return len(self._items)

def is_word_valid(word, rules):
    """
    Determine if a given word is valid based on a set of rules.
    
    Args:
        word (str): The word to validate.
        rules (list): A list of validation rules to apply.
    
    Returns:
        bool: True if the word is valid according to all rules, False otherwise.
    
    Rules can include:
    - min_length: Minimum allowed length of the word
    - max_length: Maximum allowed length of the word
    - allowed_chars: List of allowed characters
    - starts_with: List of allowed starting characters
    - ends_with: List of allowed ending characters
    """
    # Validate input types
    if not isinstance(word, str):
        return False
    
    if not isinstance(rules, dict):
        return False
    
    # Check minimum length
    if 'min_length' in rules:
        if len(word) < rules['min_length']:
            return False
    
    # Check maximum length
    if 'max_length' in rules:
        if len(word) > rules['max_length']:
            return False
    
    # Check allowed characters
    if 'allowed_chars' in rules:
        if not all(char in rules['allowed_chars'] for char in word):
            return False
    
    # Check starting characters
    if 'starts_with' in rules:
        if not any(word.startswith(start) for start in rules['starts_with']):
            return False
    
    # Check ending characters
    if 'ends_with' in rules:
        if not any(word.endswith(end) for end in rules['ends_with']):
            return False
    
    return True