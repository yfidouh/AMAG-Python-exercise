import sys
from amag_op.cli import cli;

def main(args):
    cli(args)


if __name__ == '__main__':
    print('in main')
    main(sys.argv[1:])