import warnings
import sys
from amag_op.cli.cli import cli
from amag_op.ops.amag_op import call_func

warnings.simplefilter(action="ignore", category=FutureWarning)


def main(args):
    args = cli(args)
    call_func(args)


if __name__ == "__main__":
    try:
        main(sys.argv[1:])

    except Exception as e:
        print(e)
