import argparse

import tinyfetch
from tinyfetch import core, module


def main() -> None:
    parser = argparse.ArgumentParser(
        prog="tinyfetch",
        description="Python and system information command-line fetch tool",
    )
    parser.add_argument(
        "--title-color",
        default="blue",
        choices=list(c.name for c in module.Color),
        help="set default the title color",
    )
    parser.add_argument(
        "--no-color",
        action="store_true",
        help="turn off all colors and disables",
    )
    parser.add_argument(
        "--version",
        action="version",
        version="%(prog)s v{}".format(tinyfetch.__version__),
    )
    args = parser.parse_args()

    core.render(title_color=args.title_color, no_color=args.no_color)
