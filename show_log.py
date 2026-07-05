from pathlib import Path


def show_log_file():
    """Prints the log file to the terminal when the
    -l flag is used with log in the command"""

    log_path = Path.home() / '.file_integrity_monitor' / 'change_log.txt'

    with open(f'{log_path}', 'r') as log:
        log_file = log.read()
        print(log_file)
