import requests
from typing import Dict, Any, Optional

def send_http_post_request(
    url: str, 
    data: Optional[Dict[str, Any]] = None, 
    headers: Optional[Dict[str, str]] = None, 
    timeout: int = 10
) -> Dict[str, Any]:
    """
    Send an HTTP POST request to the specified URL.

    Args:
        url (str): The target URL to send the POST request to.
        data (dict, optional): A dictionary of data to send in the request body. Defaults to None.
        headers (dict, optional): A dictionary of HTTP headers to include. Defaults to None.
        timeout (int, optional): Request timeout in seconds. Defaults to 10.

    Returns:
        dict: A dictionary containing the response data.

    Raises:
        ValueError: If the URL is empty or invalid.
        requests.exceptions.HTTPError: For HTTP error responses.
        requests.RequestException: For network-related errors.
    """
    # Validate URL
    if not url or not url.startswith(('http://', 'https://')):
        raise ValueError("Invalid or empty URL provided")

    # Use empty dict as default for optional parameters
    data = data or {}
    headers = headers or {}

    # Send the POST request
    response = requests.post(
        url, 
        json=data, 
        headers=headers, 
        timeout=timeout
    )

    # Raise an exception for HTTP error responses
    response.raise_for_status()

    # Return response as dictionary
    return {
        'status_code': response.status_code,
        'json': response.json() if response.content else {},
        'headers': dict(response.headers)
    }