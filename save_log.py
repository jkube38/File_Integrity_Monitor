import shutil
from pathlib import Path
from datetime import datetime


def save_log_file(save):

    save_path = Path(save)
    log_path = Path.home() / '.file_integrity_monitor' / 'change_log.txt'
    file_name = f'fim_change_log_{datetime.now()}.txt'
    full_save_path = f'{save_path}/{file_name}'
    full_save_path = Path(save_path) / file_name

    if save_path.exists() and save_path.is_dir():
        try:
            shutil.copy2(log_path, full_save_path)
            print(f'Succesfully saved log file to: {full_save_path}')
        except Exception as e:
            print(f'Failed to copy file: {e}. Please try a different path.')
    else:
        print('The file destination path does not exist please check your path and try again.')
