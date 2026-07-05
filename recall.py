from pathlib import Path
from create_dir import create_file_repo
from hash_generator import file_assembly


def check_for_recall(path):
    """checks for initial hash repo in users hidden directory
    if its not there it creates one."""

    path = Path(path)
    dir_name = path.name
    file_path = Path.home() / '.file_integrity_monitor' / f'{dir_name}.py'
    hash_repo = Path.home() / '.file_integrity_monitor'

    hash_list = file_assembly(path)

    if hash_repo.exists():
        pass
    else:
        create_file_repo()

    if path.exists():
        if file_path.exists():
            pass
        else:
            with open(file_path, 'x') as file:
                file.write(f'{dir_name}_list = {str(hash_list)}')
    return hash_list
