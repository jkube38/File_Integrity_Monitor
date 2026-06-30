import os
from getpass import getuser
from create_dir import create_file_repo
from hash_generator import file_assembly


def check_for_recall(path):
    """checks for initial hash repo is users hidden directory
    in not there it creates one, the checks for the recall file
    if thats not there it creates one."""

    user = getuser()
    file_path = f'{str(path)}.py'
    hash_repo = f'/Users/{user}/.file_integrity_monitor'

    if os.path.exists(hash_repo):
        pass
    else:
        create_file_repo()

    if os.path.exists(file_path):
        pass
    else:
        file_assembly(path)
