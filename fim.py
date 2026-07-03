import argparse
import sys
from compare import polling_changes


def create_parser():
    "Returns an instance of argparse.ArgumentParser"
    parser = argparse.ArgumentParser(description='''Requires a full filepath
                                     to inspect files for changes and alerts
                                     you if any are found.''')
    parser.add_argument('-l', '--log', help='Use to view the log files')
    parser.add_argument('path', help='''use to check a directories files
                        for changes (must be full path)!!!''')
    return parser


def main(args):
    '''File Integrity Monitor'''
    '''takes command line arguments to run the fim program'''
    parser = create_parser()
    ns = parser.parse_args(args)

    path = ns.path
    log = ns.log

    if not ns:
        parser.print_usage()
        sys.exit(1)
    if path:
        polling_changes(path)
    else:
        show_log_file()



if __name__ == "__main__":
    main(sys.argv[1:])
