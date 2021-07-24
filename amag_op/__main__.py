import warnings
import sys
from amag_op.cli.cli import cli

warnings.simplefilter(action="ignore", category=FutureWarning)


def main(args):
    cli(args)


if __name__ == "__main__":
    try:
        main(sys.argv[1:])
    except Exception as e:
        print(e)
