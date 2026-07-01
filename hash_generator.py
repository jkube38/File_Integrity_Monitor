import hashlib
import os
from pathlib import Path


files = []


def file_assembly(path):
    """Takes in a directory path and searches for files and creates a list of
    dictionaries containing the file name, full path, empty hash key,
    then sends the files list to gen_original_hash to create
    hashes for the files"""

    sys_path = Path(path)

    try:
        for f in sys_path.iterdir():
            if os.path.isfile(f):
                f_name = os.path.basename(f)
                files.append({'file_name': f_name, 'path': f, 'hash': ''})
            # elif os.path.isdir(f):
            # print(f"DIR: {os.path.basename(f)}")
    except FileNotFoundError:
        print('File not found please check you path and try again!!!')

    hashed_files = gen_original_hash(files)
    return hashed_files


def gen_original_hash(file_list):
    """Takes in the file list from file_assembly and generates hashes
    for each file and adds them to the files dictionary, then saves a file
    in the hidden file_integrity_monitor directory for later comparison"""

    for doc in file_list:
        p = doc['path']
        hasher = hashlib.sha256()
        with open(p, 'rb') as f:
            for piece in iter(lambda: f.read(), b""):
                hasher.update(piece)
                if not doc['hash']:
                    doc['hash'] = hasher.hexdigest()
                else:
                    print('what the f*&%')

    return file_list
