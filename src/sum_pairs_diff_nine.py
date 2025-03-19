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

    # Track the sum of pairs with difference of 9
    total_sum = 0

    # Use a set for O(n) lookup time
    number_set = set(numbers)

    # Check for pairs with difference of 9
    for num in numbers:
        # Check if num + 9 exists in the set
        if num + 9 in number_set:
            total_sum += num + (num + 9)
        # Check if num - 9 exists in the set 
        # (to avoid double counting, use only one direction)
        elif num - 9 in number_set and num > num - 9:
            total_sum += num + (num - 9)

    return total_sum