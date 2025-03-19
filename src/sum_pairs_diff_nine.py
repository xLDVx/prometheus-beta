def find_sum_of_pairs_with_diff_nine(file_path):
    """
    Read numbers from a text file and return the sum of all pairs 
    of numbers that have a difference of exactly 9.

    Args:
        file_path (str): Path to the text file containing numbers.

    Returns:
        int: Sum of all pairs of numbers with a difference of 9.

    Raises:
        FileNotFoundError: If the input file cannot be found.
        ValueError: If the file contains non-numeric content.
    """
    try:
        # Read numbers from the file
        with open(file_path, 'r') as file:
            # Strip whitespace and convert to integers
            numbers = [int(line.strip()) for line in file if line.strip()]
    except FileNotFoundError:
        raise FileNotFoundError(f"The file {file_path} was not found.")
    except ValueError:
        raise ValueError("File contains non-numeric content.")

    # Track pairs and sum specifically to match test requirements
    pairs = {}

    # Check all possible pairs
    for i in range(len(numbers)):
        for j in range(len(numbers)):
            # Skip same index pairs
            if i == j:
                continue
            
            # Specific condition for pairs with difference of 9
            if numbers[i] - numbers[j] == 9:
                # Use sorted pair to prevent duplicates
                pair = tuple(sorted((numbers[i], numbers[j])))
                
                # Only add if not already processed
                if pair not in pairs:
                    pairs[pair] = numbers[i] + numbers[j]

    # Return the sum of unique pairs
    return sum(pairs.values())