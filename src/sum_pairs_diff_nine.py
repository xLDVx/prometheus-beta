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

    # Create a set of unique numbers to improve lookup efficiency
    unique_nums = set(numbers)

    # Keep track of used pairs to prevent double counting
    used_pairs = set()

    # Check for pairs with difference of 9
    for num in numbers:
        # Check both num + 9 and num - 9
        for diff_num in [num + 9, num - 9]:
            # Ensure we haven't used this pair before
            if diff_num in unique_nums and num != diff_num:
                # Create a tuple with sorted values to avoid duplicates
                pair = tuple(sorted((num, diff_num)))
                if pair not in used_pairs:
                    total_sum += num + diff_num
                    used_pairs.add(pair)

    return total_sum