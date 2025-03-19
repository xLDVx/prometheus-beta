def validate_ip_address(ip_string: str) -> bool:
    """
    Validate if a given string is a valid IP address in the format A.B.C.D,
    where A, B, C, and D are single digit numeric characters between 0 and 9.
    
    Args:
        ip_string (str): The input string to validate as an IP address
    
    Returns:
        bool: True if the string is a valid IP address, False otherwise
    
    Examples:
        >>> validate_ip_address('1.2.3.4')
        True
        >>> validate_ip_address('01.2.3.4')
        False
        >>> validate_ip_address('1.2.3.400')
        False
    """
    # Check if the input is a string
    if not isinstance(ip_string, str):
        return False
    
    # Split the IP address into octets
    octets = ip_string.split('.')
    
    # Check if there are exactly 4 octets
    if len(octets) != 4:
        return False
    
    # Validate each octet
    for octet in octets:
        # Check if octet is exactly 1 character long
        if len(octet) != 1:
            return False
        
        # Check if octet is a digit between 0 and 9
        if not (octet.isdigit() and 0 <= int(octet) <= 9):
            return False
    
    return True