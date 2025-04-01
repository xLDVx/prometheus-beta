import os
import pytest
import requests
from src.file_downloader import download_file

def test_download_file_with_default_destination(tmp_path):
    # Use a small, reliable file for testing
    test_url = "https://raw.githubusercontent.com/pytest-dev/pytest/main/README.rst"
    
    # Change current working directory to temporary path
    os.chdir(tmp_path)
    
    # Create downloads directory
    os.makedirs('downloads', exist_ok=True)
    
    # Download file
    downloaded_path = download_file(test_url)
    
    # Assertions
    assert os.path.exists(downloaded_path)
    assert os.path.getsize(downloaded_path) > 0

def test_download_file_with_custom_destination(tmp_path):
    # Use a small, reliable file for testing
    test_url = "https://raw.githubusercontent.com/pytest-dev/pytest/main/README.rst"
    
    # Change current working directory to temporary path
    os.chdir(tmp_path)
    
    # Custom destination
    custom_path = 'test_download/pytest_readme.rst'
    
    # Download file
    downloaded_path = download_file(test_url, custom_path)
    
    # Assertions
    assert os.path.exists(downloaded_path)
    assert os.path.getsize(downloaded_path) > 0
    assert downloaded_path.endswith('pytest_readme.rst')

def test_download_invalid_url():
    with pytest.raises(ValueError):
        download_file("")
    
    with pytest.raises(ValueError):
        download_file(None)

def test_download_non_existent_url():
    with pytest.raises(requests.RequestException):
        download_file("https://nonexistent.example.com/nosuchfile.txt")

def test_invalid_url_type():
    with pytest.raises(ValueError):
        download_file(123)  # Not a string