import os
from getpass import getuser
from recall import check_for_recall


def file_to_file(path):
    init_run = check_for_recall(path)
    user = getuser()
    filename = f'{path.split('/')[-1]}.py'
    recall_hash_path = f'/Users/{user}/.file_integrity_monitor/{filename}.py'
