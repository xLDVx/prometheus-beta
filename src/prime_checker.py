def is_prime(number: int) -> bool:
    """
    Determine whether the input integer is a prime number.

    A prime number is a natural number greater than 1 that is only divisible by 1 and itself.

    Args:
        number (int): The number to check for primality.
                      Must be an integer between 2 and 1000 (inclusive).

    Returns:
        bool: True if the number is prime, False otherwise.

    Raises:
        ValueError: If the input is not an integer between 2 and 1000.
    """
    # Validate input range
    if not isinstance(number, int):
        raise ValueError("Input must be an integer")
    
    if number < 2 or number > 1000:
        raise ValueError("Input must be between 2 and 1000")
    
    # Special case for 2 (the only even prime number)
    if number == 2:
        return True
    
    # Even numbers greater than 2 are not prime
    if number % 2 == 0:
        return False
    
    # Check odd divisors up to the square root of the number
    # This is an optimization to reduce computational complexity
    for divisor in range(3, int(number**0.5) + 1, 2):
        if number % divisor == 0:
            return False
    
    return True