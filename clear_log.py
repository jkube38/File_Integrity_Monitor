import sys
from pathlib import Path


def clear_log_file():
    '''When the -c flag is passed into the fim command the log file
    is erased and reset'''

    # log_path = f'/Users/{user}/.file_integrity_monitor/change_log.txt'
    base_path = Path.home()
    log_path = base_path / '.file_integrity_monitor' / 'change_log.txt'

    verify = input(
        "Are you sure? Did you remember to save? This will permanently erase your logs, proceed with erasing (y/n):\n"
        )

    if verify == 'n':
        print("Your logs will not be erased. Run with -s and full filepath to desired directory to save log file.")
        sys.exit()
    elif verify == 'y':
        with open(log_path, 'w') as log_file:
            log_file.write('')
        print("Log file erased and ready for a fresh start.")
