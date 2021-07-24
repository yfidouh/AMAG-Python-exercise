import argparse


def add_operate_subparser(subparsers):
    # parser for operating on two floats
    parser_1 = subparsers.add_parser("operate", help="perform an operation on x and y")
    parser_1.add_argument("x", type=float, help="the first float argument")
    parser_1.add_argument("y", type=float, help="the second float argument")
    parser_1.add_argument("op", type=str, help="the operation name")
    # return subparsers


def add_process_subparser(subparsers):
    # parser for processing a file containing rows of floats
    parser_2 = subparsers.add_parser(
        "process", help="process an excel or csv file with x, y and operation columns"
    )
    parser_2.add_argument("file", type=argparse.FileType("r"))
    parser_2.add_argument(
        "-s", "-sheet", type=str, default=None, help="Excel sheetname"
    )


def create_cli_parser():
    parser = argparse.ArgumentParser(prog="amag_op", description="Process some floats.")
    subparsers = parser.add_subparsers()
    add_process_subparser(subparsers)
    add_operate_subparser(subparsers)
    return parser


def cli(args):
    parser = create_cli_parser()
    if len(args) > 0:
        args = parser.parse_args(args)
    else:
        # to display the script options when no arguments have been provided
        args = parser.parse_args(["--help"])
    return args
