import os
import pytest
import tarfile
import shutil

from src.tar_extractor import extract_tar_archive

@pytest.fixture
def sample_tar_archive(tmp_path):
    """Create a sample tar archive for testing."""
    # Create some test files
    d = tmp_path / "test_dir"
    d.mkdir()
    
    files = [
        (d / "file1.txt", "Content of file 1"),
        (d / "file2.txt", "Content of file 2"),
        (d / "nested" / "file3.txt", "Content of file 3")
    ]
    
    # Ensure nested directory exists
    files[2][0].parent.mkdir(parents=True)
    
    # Write test files
    for file_path, content in files:
        file_path.write_text(content)
    
    # Create tar archive
    archive_path = tmp_path / "test_archive.tar"
    with tarfile.open(archive_path, "w") as tar:
        tar.add(d, arcname=os.path.basename(d))
    
    return archive_path

def test_extract_all_files(sample_tar_archive, tmp_path):
    """Test extracting all files from a tar archive."""
    extract_path = tmp_path / "extract_all"
    extracted = extract_tar_archive(str(sample_tar_archive), str(extract_path))
    
    assert len(extracted) == 3  # file1.txt, file2.txt, nested/file3.txt
    assert all(os.path.exists(file) for file in extracted)

def test_extract_specific_files(sample_tar_archive, tmp_path):
    """Test extracting specific files from a tar archive."""
    extract_path = tmp_path / "extract_specific"
    extracted = extract_tar_archive(
        str(sample_tar_archive), 
        str(extract_path), 
        specific_files=["test_dir/file1.txt"]
    )
    
    assert len(extracted) == 1
    assert os.path.basename(extracted[0]) == "file1.txt"

def test_extract_default_path(sample_tar_archive, tmp_path):
    """Test extracting to default path when no path specified."""
    os.chdir(tmp_path)
    extracted = extract_tar_archive(str(sample_tar_archive))
    
    assert len(extracted) == 3
    assert all(os.path.exists(file) for file in extracted)

def test_non_existent_archive():
    """Test handling of non-existent archive."""
    with pytest.raises(FileNotFoundError):
        extract_tar_archive("/path/to/non/existent/archive.tar")

def test_invalid_tar_file(tmp_path):
    """Test handling of invalid tar file."""
    invalid_file = tmp_path / "invalid.tar"
    invalid_file.write_text("This is not a tar file")
    
    with pytest.raises(ValueError):
        extract_tar_archive(str(invalid_file))

def test_extract_non_existent_specific_files(sample_tar_archive, tmp_path):
    """Test extracting files that do not exist in the archive."""
    extract_path = tmp_path / "extract_non_existent"
    extracted = extract_tar_archive(
        str(sample_tar_archive), 
        str(extract_path), 
        specific_files=["non_existent_file.txt"]
    )
    
    assert len(extracted) == 0