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

    # Sum of pairs
    total_sum = 0

    # Check for pairs with difference of 9
    # Using frequency dictionary to handle duplicate cases
    from collections import defaultdict
    freq = defaultdict(int)
    for num in numbers:
        freq[num] += 1

    # Track unique pairs to avoid double counting
    unique_pairs = set()

    for num in numbers:
        # Check for num - 9 specifically
        if num - 9 in freq:
            pair = (num - 9, num)
            
            # Only process if this pair hasn't been counted before
            if pair not in unique_pairs:
                # Perform multiple times based on frequency 
                # of the involved numbers
                count = min(freq[num], freq[num-9])
                
                # Add to total sum and mark as processed
                total_sum += (num + (num-9)) * count
                unique_pairs.add(pair)

    return total_sum