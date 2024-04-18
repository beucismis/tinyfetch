import argparse
from json import dumps as json_dumps

import tinyfetch
from tinyfetch import core, module

parser = argparse.ArgumentParser(
    prog="tinyfetch",
    description="Python and system information command-line fetch tool",
)
parser.add_argument(
    "--title-color",
    default="white",
    choices=list(c.name for c in module.Color),
    help="set default the title color",
)
parser.add_argument(
    "--no-color",
    action="store_true",
    help="turn off all colors and disables",
)
parser.add_argument(
    "--no-logo",
    action="store_true",
    help="turn off logo and disables",
)
parser.add_argument(
    "--json",
    action="store_true",
    help="output to json and exit",
)
parser.add_argument(
    "--version",
    action="version",
    version="%(prog)s v{}".format(tinyfetch.__version__),
)


def main(args=None) -> None:
    args = parser.parse_args(args)

    if args.json:
        output: list = []
        for module_obj in core.modules_list:
            dict_obj = module_obj.__call__(no_color=True).to_dict()
            if dict_obj is None:
                continue
            output.append(dict_obj)
        return json_dumps(output)

    core.render(
        title_color=args.title_color, no_color=args.no_color, no_logo=args.no_logo
    )


if __name__ == "__main__":
    main()
