import os
import re
import socket
import getpass
import platform
from pathlib import Path
from pip import __version__ as pip__version__
from pip._internal.operations.freeze import freeze


__version__ = "0.14.0"
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


def red(text):
    return BOLD + RED + text + RESET


def get_linux_os_name():
    for p in Path("/").glob("etc/*release"):
        with p.open() as file:
            match = [DISTRO_NAME_RE.match(l) for l in file.readlines()][0]

        if match:
            return match.group(1) if match.group(1) != "" or None else SPACE


def render(info, ascii_logo):
    if len(ascii_logo) < len(info):
        for _ in range(len(info) - len(ascii_logo)):
            ascii_logo.append(SPACE * len(ascii_logo[0]))

    elif len(ascii_logo) > len(info):
        for _ in range(len(ascii_logo) - len(info)):
            info.append(SPACE)

    for (art_line, info_line) in zip(ascii_logo, info):
        print("{} {}".format(art_line, info_line))


def main():
    os_type = platform.system()

    if os_type == "Windows":
        # https://docs.python.org/3/library/getpass.html#getpass.getuser
        userinfo = f"{red(getpass.getuser())}@{red(socket.gethostname())}"
        splitline = (len(getpass.getuser()) + len(socket.gethostname()) + 1) * "─"

        # information on the os
        kernel = f"{red('Kernel')}:"
        operating_system = f"{red('OS')}: Windows {platform.version()}"

    elif os_type == "Linux":
        uname = os.uname()
        # https://docs.python.org/3/library/getpass.html#getpass.getuser
        userinfo = f"{red(getpass.getuser())}@{red(uname.nodename)}"
        splitline = (len(getpass.getuser()) + len(uname.nodename) + 1) * "─"

        # information on the os
        kernel = f"{red('Kernel')}: {uname.sysname}-{uname.release}"
        operating_system = f"{red('OS')}: {get_linux_os_name()} {uname.machine}"

    elif os_type == "Darwin":  # darwin refers to mac os
        # os.uname method can be used however the bash env variable is used
        # instead to accomodate for the user altering their hostname variable
        hostname = os.environ["HOSTNAME"]
        userinfo = f"{red(getpass.getuser())}@{red(hostname)}"
        splitline = (len(getpass.getuser()) + len(hostname) + 1) * "─"

        #information on the os
        uname = os.uname()
        version = platform.mac_ver()[0]
        kernel = f"{red('Kernel')}: {uname.sysname}-{uname.release}"
        operating_system = f"{red('OS')}: Mac OS X {version} {uname.machine}"

    # information on python
    python_version = f"{red('Python Version')}: {platform.python_version()}"
    pip_version = f"{red('PIP Version')}: {pip__version__}"
    pip_packages = f"{red('PIP Packages')}: {sum(1 for p in freeze(local_only=True))}"
    implementation = f"{red('Implementation')}: {platform.python_implementation()}"
    compiler = f"{red('Compiler')}: {platform.python_compiler()}"

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
            operating_system,
            SPACE,
            "".join(dark_colors) + RESET,
            "".join(bright_colors) + RESET,
            SPACE,
        ],
        ASCII_LOGO,
    )


if __name__ == "__main__":
    main()
