import argparse
import sys
from compare import polling_changes
from show_log import show_log_file


def create_parser():
    "Returns an instance of argparse.ArgumentParser"
    parser = argparse.ArgumentParser(description='''Requires a full filepath to inspect files in a directory for
                                    changes and alerts you if any are found, using flags, the log files can be viewed
                                     and reset, and the poling time can also be set to your desired time in seconds''')
    parser.add_argument('-l', '--log', help='Use to view the log files, the flags must be followed by log as an arg.')
    parser.add_argument('-p', '--path', help='''use to check a directories files for changes (must be full path)!!!''')
    return parser


def main(args):
    '''File Integrity Monitor'''
    '''takes command line arguments to run the fim program'''
    parser = create_parser()
    ns = parser.parse_args(args)

    path = ns.path
    log = ns.log
    print(ns)
    if not ns:
        parser.print_usage()
        sys.exit(1)
    if path:
        polling_changes(path)
    elif log:
        show_log_file()


if __name__ == "__main__":
    main(sys.argv[1:])
