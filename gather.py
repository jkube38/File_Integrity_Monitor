import pathlib
import sys
from getpass import getuser
import importlib.util
from recall import check_for_recall
import builtins
builtins.PosixPath = pathlib.PurePosixPath


def gather_hash_files(path):

    current_list = check_for_recall(path)
    # variables and paths for accessing files
    user = getuser()
    filename = f'{path.split('/')[-1]}'
    recall_hash_path = pathlib.Path(
        f'/Users/{user}/.file_integrity_monitor/{filename}.py')

    # imports the previouly used list from hash repo to compare previous
    # version with current version of the directory
    try:
        spec = importlib.util.spec_from_file_location('external_list',
                                                      recall_hash_path)
        my_data = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(my_data)
        recall_list = getattr(my_data, f'{filename}_list')
    except FileNotFoundError:
        print('Error: The specified file could not be found.')
        sys.exit()
    except AttributeError:
        print(
            "Error: The module loaded, but the variable name you requested"
            " doesn't exist inside it")
        sys.exit()

    return current_list, recall_list
