import os
from create_cbmo4ers_backend import create_files

# test_create_cbmo4ers_backend.py


def test_create_files_creates_structure(tmp_path):
    # Minimal structure for test
    structure = {
        "dir1": {
            "file1.txt": "hello",
            "file2.txt": "world"
        },
        "file3.txt": "!"
    }
    create_files(tmp_path, structure)
    # Check directories
    assert (tmp_path / "dir1").is_dir()
    # Check files
    assert (tmp_path / "dir1" / "file1.txt").is_file()
    assert (tmp_path / "dir1" / "file2.txt").is_file()
    assert (tmp_path / "file3.txt").is_file()
    # Check contents
    assert (tmp_path / "dir1" / "file1.txt").read_text(encoding="utf-8") == "hello"
    assert (tmp_path / "dir1" / "file2.txt").read_text(encoding="utf-8") == "world"
    assert (tmp_path / "file3.txt").read_text(encoding="utf-8") == "!"