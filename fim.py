import hashlib
import os
import argparse
import sys
import subprocess
from pathlib import Path
# from time import sleep, strftime


# dir_to_read = Path("/Users/kube/PersonalProjects/codewars/")
# files = []
# dirs = []


def file_assembly(path):
    """Takes in a directory path and searches for files and creates a list of
    dictionaries containing the file name, full path, empty hash key,
    then sends the files list to gen_original_hash to create
    hashes for the files"""
    files = []
    sys_path = Path(path)
    for f in sys_path.iterdir():
        if os.path.isfile(f):
            f_name = os.path.basename(f)
            files.append({'file_name': f_name, 'path': f, 'hash': ''})
        # elif os.path.isdir(f):
        # print(f"DIR: {os.path.basename(f)}")

    gen_original_hash(files)
    return files


def gen_original_hash(file_list):
    """Takes in the file list from file_assembly and generates hashes
    for each file and adds them to the files dictionary"""
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

    for i in file_list:
        print(i)

    return file_list


def create_parser():
    "Returns an instance of argparse.ArgumentParser"
    parser = argparse.ArgumentParser(description='''Requires a full filepath
                                     to inspect files for changes and alerts
                                     you if any are found.''')
    parser.add_argument('path', help='''use to check a directories files
                        for changes (must be full path)!!!''')
    return parser


def main(args):
    '''File Integrity Monitor'''
    '''takes command line arguments to run the fim program'''

    parser = create_parser()
    ns = parser.parse_args(args)

    path = ns.path

    if not ns:
        parser.print_usage()
        sys.exit(1)

    file_assembly(path)

    # subprocess.run()


if __name__ == "__main__":
    main(sys.argv[1:])
