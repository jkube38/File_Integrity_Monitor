from pathlib import Path


def create_file_repo():
    """Creates a hidden directory in the users home directory
    to save the lists to access after the program closes to maintain
    original hashes"""

    path_dir = Path.home() / '.file_integrity_monitor'
    if not path_dir.exists():
        path_dir.mkdir()
