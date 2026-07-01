import argparse
import sys
from compare import compare_versions


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

    compare_versions(path)


if __name__ == "__main__":
    main(sys.argv[1:])
