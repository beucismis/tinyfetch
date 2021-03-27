import os
import psutil
import platform
import subprocess
from colorama import Fore, Style
from pip import __version__ as pip__version__


__version__ = "0.2.1"
__license__ = "GPL-3.0"
__author__ = "Adil Gurbuz"
__contact__ = "beucismis@tutamail.com"
__source__ = "https://github.com/beucismis/pythonfetch"
__description__ = "Python and system information command-line tool"

this_dir, this_filename = os.path.split(__file__)

SPACE = " "
D_COLORS = [
    Fore.RED,
    Fore.YELLOW,
    Fore.GREEN,
    Fore.CYAN,
    Fore.BLUE,
    Fore.MAGENTA,
    Fore.BLACK,
    Fore.WHITE,
]
B_COLORS = [
    Fore.LIGHTRED_EX,
    Fore.LIGHTYELLOW_EX,
    Fore.LIGHTGREEN_EX,
    Fore.LIGHTCYAN_EX,
    Fore.LIGHTBLUE_EX,
    Fore.LIGHTMAGENTA_EX,
    Fore.LIGHTBLACK_EX,
    Fore.LIGHTWHITE_EX,
]


with open(os.path.join(this_dir, "data/ascii-art.txt")) as file:
    ART = [SPACE + line.replace("\n", "") for line in file.readlines()]


def red(text):
    return Fore.LIGHTRED_EX + text + Style.RESET_ALL


def exc(command):
    sp = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE)
    return sp.stdout.read().decode("utf-8").replace("\n", "")


def render(info):
    for (art_line, info_line) in zip(ART, info):
        print("{}   {}".format(art_line, info_line))


def main():
    uname = os.uname()
    mem = psutil.virtual_memory()
    mem_total = round(mem.total / 1048576)
    mem_used = round(mem.used / 1048576)

    gcc_ver = exc("gcc --version | grep gcc | awk '{print $4}'")
    python_ver = platform.python_version()
    pip_ver = pip__version__
    pip_packages = " "  # TODO: pip3 list | wc -l

    userinfo = "{}{}{}".format(red(os.getlogin()), "@", red(uname.nodename))
    splitline = "═" * (len(os.getlogin()) + len(uname.nodename) + 1)

    gcc_ver = "{}: {}".format(red("gcc ver"), gcc_ver)
    python_ver = "{}: {}".format(red("python ver"), python_ver)
    pip_ver = "{}: {}".format(red("pip ver"), pip_ver)
    pip_packages = "{}: {}".format(red("pip packages"), pip_packages)

    os_ = "{}: {}".format(red("os"), uname.version)
    kernel = "{}: {}".format(red("kernel"), uname.release)
    cpu = "{}: {}".format(red("cpu"), platform.processor())
    ram = "{}: {} / {} {}".format(red("ram"), mem_used, mem_total, "MiB")

    bright_colors = [color + "███" for color in B_COLORS]
    dark_colors = [color + "███" for color in D_COLORS]

    render(
        [
            SPACE,
            SPACE,
            userinfo,
            splitline,
            gcc_ver,
            python_ver,
            pip_ver,
            pip_packages,
            os_,
            kernel,
            cpu,
            ram,
            SPACE,
            "".join(bright_colors) + Style.RESET_ALL,
            "".join(dark_colors) + Style.RESET_ALL,
            SPACE,
            SPACE,
        ]
    )


if __name__ == "__main__":
    main()
