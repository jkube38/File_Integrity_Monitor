import copy
import time
from pathlib import Path
from getpass import getuser
from datetime import datetime
from gather import gather_hash_files


def compare_versions(path):
    # runs the gather hash function to return 2 lists to compare
    # get the lengths of both lists for comparison
    current_list, recall_list = gather_hash_files(path)
    # cur_len = len(current_list)
    # rec_len = len(recall_list)

    # variables used for path variables and writing to files
    present_time = datetime.now()

    # paths used for writing log entries, updating recall lists
    # and using the target path for reference
    target_dir = Path(path)
    base_path = Path.home() / '.file_integrity_monitor'

    if target_dir.exists():
        directory = Path(str(current_list[0]['path'])).parent.name

        # creates a copy of the current list to use for verifictation of file removal
        rec_lst_copy = copy.deepcopy(recall_list)
        cur_lst_copy = copy.deepcopy(current_list)

        # loops through current list handling filename changes, file alterations and
        # file creations
        for dict in current_list:
            hash_search = [h for h in recall_list if dict['hash'] == h['hash'] and dict['hash'] != '']
            fname_search = [fn for fn in recall_list if dict['file_name'] == fn['file_name']]

            if dict in recall_list:
                rec_lst_copy = [d for d in rec_lst_copy if d != dict]
            elif hash_search:
                # alerts to terminal of the filename change and updates the log file
                print(f'--- !NAME CHANGE ALERT! -- FILE: {hash_search[0]['file_name']} '
                      f'has been changed to {dict['file_name']}'
                      )
                rec_lst_copy = [d for d in rec_lst_copy if d.get('hash') != dict['hash']]
                with open(base_path / 'change_log.txt', 'a') as file:
                    file.write(f'{hash_search[0]['file_name']} was CHANGED to {dict['file_name']},'
                               f' @ {dict['path']} alteration caught at {present_time}, actual '
                               'alteration time will not match\n\n'
                               )
            elif fname_search:
                # alerts to terminal of the file alteration and updates the log file
                print(f'--- !ALTERATION ALERT! -- FILE CHANGE: {fname_search[0]['file_name']} has been alterted')
                rec_lst_copy = [d for d in rec_lst_copy if d.get('file_name') != dict['file_name']]
                with open(base_path / 'change_log.txt', 'a') as file:
                    file.write(f'{dict['file_name']} has been ALTERED,'
                               f' @ {dict['path']}, alteration caught at {present_time}, actual '
                               'alteration time will not match\n\n'
                               )
            else:
                # alerts to terminal of the file creation and updates the log file
                print(f'--- !CREATION ALERT! -- FILE: {dict['file_name']} has been created')
                with open(base_path / 'change_log.txt', 'a') as file:
                    file.write(f'{dict['file_name']} has been CREATED,'
                               f' @ {dict['path']}, alteration caught at {present_time}, actual '
                               'alteration time will not match\n\n'
                               )
            cur_lst_copy.remove(dict)

        if cur_lst_copy:
            print(f'remaining current files: {cur_lst_copy}')
        # if the recall length is greater than the current length it will take whatss
        # left in the copied recall list and send alert to the terminal and update log file
        if rec_lst_copy:
            for dict in rec_lst_copy:
                print(f'--- !REMOVAL ALERT! -- FILE: {dict['file_name']} has been removed')
                with open(base_path / 'change_log.txt', 'a') as file:
                    file.write(f'{dict['file_name']} had been REMOVED, @ {dict['path']},'
                               f' alteration caught at {present_time}, actual alteration time will'
                               ' not match\n\n'
                               )
        # updates the recall list to match the new one
        with open(base_path / f'{directory}.py', 'w') as file:
            file.write(f'{directory}_list = {current_list}')


def polling_changes(path):
    user = getuser()
    try:
        path = Path(path)
        if path.exists():
            duration = input(f'Hello {user}; How long would you like the polling intervals to be (in seconds).\n')
            directory = Path(path).stem
            print(f'Actively scanning \033[3m{directory}\033[0m directory...........{datetime.now()}')
            while True:
                compare_versions(path)
                time.sleep(int(duration))
        else:
            print(f'Your path: \033[3m{path}\33[0m does not exist please check it and try again.')
    except KeyboardInterrupt:
        print(f'\033[3m   Goodbye {user}!!\033[0m')
