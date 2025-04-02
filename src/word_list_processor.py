def process_word_list(input_file_path):
    """
    Read a text file, remove duplicate words, and return a sorted list of unique words.

    Args:
        input_file_path (str): Path to the input text file containing words.

    Returns:
        list: A sorted list of unique words from the input file.

    Raises:
        FileNotFoundError: If the input file does not exist.
        IOError: If there's an issue reading the file.
    """
    try:
        # Read the file and split into words
        with open(input_file_path, 'r') as file:
            # Read all lines, strip whitespace, convert to lowercase
            words = [word.strip().lower() for word in file.readlines()]
        
        # Remove duplicates by converting to a set, then back to a sorted list
        unique_words = sorted(set(words))
        
        return unique_words
    
    except FileNotFoundError:
        raise FileNotFoundError(f"Input file not found: {input_file_path}")
    except IOError as e:
        raise IOError(f"Error reading file {input_file_path}: {e}")