import os
import requests

def download_file(url, destination=None):
    """
    Download a file from a given URL.

    Args:
        url (str): The URL of the file to download.
        destination (str, optional): The path where the file should be saved. 
                                     If not provided, uses the filename from the URL.

    Returns:
        str: The full path to the downloaded file.

    Raises:
        ValueError: If the URL is invalid or empty.
        requests.RequestException: For network-related errors.
        IOError: For file writing errors.
    """
    # Validate URL
    if not url or not isinstance(url, str):
        raise ValueError("Invalid URL: URL must be a non-empty string")

    try:
        # Send a GET request to download the file
        response = requests.get(url, stream=True)
        response.raise_for_status()  # Raise an exception for bad status codes

        # Determine destination filename
        if destination is None:
            # Extract filename from URL or Content-Disposition header
            filename = response.headers.get('Content-Disposition', '').split('filename=')[-1] or \
                       url.split('/')[-1]
            destination = os.path.join('downloads', filename)

        # Ensure the downloads directory exists
        os.makedirs(os.path.dirname(destination), exist_ok=True)

        # Write the file
        with open(destination, 'wb') as file:
            for chunk in response.iter_content(chunk_size=8192):
                file.write(chunk)

        return os.path.abspath(destination)

    except requests.RequestException as e:
        raise requests.RequestException(f"Error downloading file from {url}: {str(e)}")
    except IOError as e:
        raise IOError(f"Error saving file to {destination}: {str(e)}")