import os
from getpass import getuser
from create_dir import create_file_repo
from hash_generator import file_assembly


def check_for_recall(path):
    """checks for initial hash repo is users hidden directory
    in not there it creates one, then checks for the recall file
    if thats not there it creates one."""

    user = getuser()
    parent = path.split('/')[-1]

    file_path = f'/Users/{user}/.file_integrity_monitor/{parent}.py'
    hash_repo = f'/Users/{user}/.file_integrity_monitor'

    hash_list = file_assembly(path)

    if os.path.exists(hash_repo):
        pass
    else:
        create_file_repo()

    if os.path.exists(file_path):
        pass
    else:
        with open(f'/Users/{user}/.file_integrity_monitor/{parent}.py',
                  'x') as file:
            file.write(f'{parent}_list = {str(hash_list)}')
    return hash_list
