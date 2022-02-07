import os
import re
import getpass
import platform
from pathlib import Path
from pip import __version__ as pip__version__
from pip._internal.operations.freeze import freeze


__version__ = "0.13.0"
__license__ = "GPL-3.0"
__author__ = "Adil Gürbüz"
__contact__ = "beucismis@tutamail.com"
__source__ = "https://github.com/beucismis/pythonfetch"
__description__ = "Python and system information command-line tool"

SPACE = " "
RESET = "\u001b[0m"
BOLD = "\u001b[1m"
BLACK = "\u001b[030m"
RED = "\u001b[031m"
GREEN = "\u001b[032m"
YELLOW = "\u001b[033m"
BLUE = "\u001b[034m"
MAGENTA = "\u001b[035m"
CYAN = "\u001b[036m"
WHITE = "\u001b[037m"
D_COLORS = [BLACK, RED, GREEN, YELLOW, BLUE, MAGENTA, CYAN, WHITE]
B_COLORS = [c[:-1] + ";1m" for c in D_COLORS]

ASCII_LOGO = [
    "                           ",
    "          ───────          ",
    "        ─{}█▀▀██████{}─        ".format(BLUE, RESET),
    "        ─{}█████████{}─        ".format(BLUE, RESET),
    "   ──────────{}█████{}─  ───   ".format(BLUE, RESET),
    " ─{}████████████████{}──{}█████{}─ ".format(BLUE, RESET, YELLOW, RESET),
    " ─{}████████████████{}──{}█████{}─ ".format(BLUE, RESET, YELLOW, RESET),
    " ─{}█████{}─────────────{}█████{}─ ".format(BLUE, RESET, YELLOW, RESET),
    " ─{}█████{}──{}████████████████{}─ ".format(BLUE, RESET, YELLOW, RESET),
    " ─{}█████{}──{}████████████████{}─ ".format(BLUE, RESET, YELLOW, RESET),
    "   ───  ─{}█████{}──────────   ".format(YELLOW, RESET),
    "        ─{}██████▀▀█{}─        ".format(YELLOW, RESET),
    "        ─{}█████████{}─        ".format(YELLOW, RESET),
    "          ───────          ",
    "                           ",
]

DISTRO_NAME_RE = re.compile('^PRETTY_NAME="([^"]+)"$')


def get_os_name():
    for p in Path("/").glob("etc/*release"):
        with p.open() as fptr:
            for line in fptr:
                match = DISTRO_NAME_RE.match(line)
                if match:
                    return match.group(1)


def red(text):
    return BOLD + RED + text + RESET


def render(info, ascii_logo):
    for (art_line, info_line) in zip(ascii_logo, info):
        print("{} {}".format(art_line, info_line))


def main():
    uname = os.uname()
    # https://docs.python.org/3/library/getpass.html#getpass.getuser
    userinfo = "{}{}{}".format(red(getpass.getuser()), "@", red(uname.nodename))
    splitline = (len(getpass.getuser()) + len(uname.nodename) + 1) * "-"

    python_version = "{}: {}".format(red("Python Version"), platform.python_version())
    pip_version = "{}: {}".format(red("PIP Version"), pip__version__)
    pip_packages = "{}: {}".format(
        red("PIP Packages"), sum(1 for p in freeze(local_only=True))
    )
    implementation = "{}: {}".format(
        red("Implementation"), platform.python_implementation()
    )
    compiler = "{}: {}".format(red("Compiler"), platform.python_compiler())

    operation_system = "{}: {}".format(
        red("OS"),
        "{} {}".format(get_os_name(), uname.machine)
        if get_os_name() != str() or None
        else SPACE,
    )
    kernel = "{}: {}".format(red("Kernel"), uname.sysname + "-" + uname.release)

    bright_colors = [color + "███" for color in B_COLORS]
    dark_colors = [color + "███" for color in D_COLORS]

    render(
        [
            SPACE,
            userinfo,
            splitline,
            python_version,
            pip_version,
            pip_packages,
            implementation,
            compiler,
            SPACE,
            kernel,
            operation_system,
            SPACE,
            "".join(dark_colors) + RESET,
            "".join(bright_colors) + RESET,
            SPACE,
        ],
        ASCII_LOGO,
    )


if __name__ == "__main__":
    main()
