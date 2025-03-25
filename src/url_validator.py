import re
from urllib.parse import urlparse

def is_valid_url(url: str) -> bool:
    """
    Validate if the given string is a well-formed URL.

    Args:
        url (str): The URL string to validate.

    Returns:
        bool: True if the URL is valid, False otherwise.

    The function checks for:
    - Proper URL structure
    - Valid scheme (http, https, ftp, etc.)
    - Non-empty netloc (domain)
    """
    # Check if input is a string and not empty
    if not isinstance(url, str) or not url.strip():
        return False

    try:
        # Use urlparse to break down the URL
        parsed_url = urlparse(url)

        # Check if scheme exists and is non-empty
        if not parsed_url.scheme:
            return False

        # Check if netloc (domain) exists and is non-empty
        if not parsed_url.netloc:
            return False

        # Additional regex validation for more robust checking
        url_regex = re.compile(
            r'^(?:http|ftp)s?://'  # http:// or https:// or ftp:// or ftps://
            r'(?:(?:[A-Z0-9](?:[A-Z0-9-]{0,61}[A-Z0-9])?\.)+(?:[A-Z]{2,6}\.?|[A-Z0-9-]{2,}\.?)|'  # domain...
            r'localhost|'  # localhost...
            r'\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})'  # ...or ip
            r'(?::\d+)?'  # optional port
            r'(?:/?|[/?]\S+)$', re.IGNORECASE)

        return bool(url_regex.match(url))

    except Exception:
        return False