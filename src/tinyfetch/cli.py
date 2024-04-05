import argparse

import tinyfetch
from tinyfetch import core


def main() -> None:
    parser = argparse.ArgumentParser(
        prog="tinyfetch",
        description="Python and system information command-line fetch tool",
    )
    parser.add_argument(
        "--version",
        action="version",
        version="%(prog)s v{}".format(tinyfetch.__version__),
    )
    args = parser.parse_args()

    if args:
        core.render()
