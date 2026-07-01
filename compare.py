from getpass import getuser
from datetime import datetime
from gather import gather_hash_files


def compare_versions(path):

    current_list, recall_list = gather_hash_files(path)
    user = getuser()
    change_log_path =

    cur_len = len(current_list)
    rec_len = len(recall_list)

    if cur_len == rec_len:
        for ind in range(cur_len):
            if current_list[ind]['hash'] == recall_list[ind]['hash']:
                print('...')
            else:
                dir = str(current_list[ind]['path']).split('/')[4]
                print(f'---- ALERT: {current_list[ind]['file_name'].upper()}'
                      f' in the {dir.upper()} directory'
                      ' has been altered!! ----')
                print('----------- updating registry, generating log entry')

                # create and or write to a log file

                present_time = datetime.now()
                with open(f'/Users/{user}/'
                          '.file_integrity_monitor/change_log.py',
                          'x') as file:
                    file.write(f'{current_list[ind]['file_name']} located at'
                               f'{str(current_list[ind]['path'])} alteration '
                               f'caught on {present_time}, actual alteration '
                               'time will not match.')
