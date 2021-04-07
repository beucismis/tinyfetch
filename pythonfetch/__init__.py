import os
import re
import psutil
import platform
import subprocess
from colorama import Fore, Style
from pip import __version__ as pip__version__
from pip._internal.operations.freeze import freeze


__version__ = "0.8.2"
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


def get_processor_name():
    if platform.system() == "Windows":
        return platform.processor()

    elif platform.system() == "Darwin":
        os.environ["PATH"] = os.environ["PATH"] + os.pathsep + "/usr/sbin"
        command = "sysctl -n machdep.cpu.brand_string"
        return subprocess.check_output(command).strip()

    elif platform.system() == "Linux":
        command = "cat /proc/cpuinfo"
        all_info = subprocess.check_output(command, shell=True)

        for line in all_info.decode().split("\n"):
            if "model name" in line:
                return re.sub(".*model name.*:", "", line, 1)

    return ""


with open(os.path.join(this_dir, "data/ascii-art.txt")) as file:
    ART = [SPACE + line.replace("\n", "") for line in file.readlines()]


def red(text):
    return Fore.LIGHTRED_EX + text + Style.RESET_ALL


def exc(command):
    sp = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE)
    return sp.stdout.read().decode("utf-8").replace("\n", "")


def render(info):
    for (art_line, info_line) in zip(ART, info):
        print("{} {}".format(art_line, info_line))


def main():
    uname = os.uname()
    mem = psutil.virtual_memory()
    mem_total = round(mem.total / 1048576)
    mem_used = round(mem.used / 1048576)

    python_ver = platform.python_version()
    pip_packages = package_count = sum(1 for p in freeze(local_only=True))
    implementation = platform.python_implementation()
    compiler = platform.python_compiler()
    os_ = exc("cat /etc/*release | grep PRETTY_NAME | cut -d= -f2 | tr -d '\"'")

    userinfo = "{}{}{}".format(red(os.getlogin()), "@", red(uname.nodename))
    splitline = "-" * (len(os.getlogin()) + len(uname.nodename) + 1)

    python_ver = "{}: {}".format(red("python ver"), python_ver)
    pip_ver = "{}: {}".format(red("pip ver"), pip__version__)
    pip_packages = "{}: {}".format(red("pip packages"), pip_packages)
    implementation = "{}: {}".format(red("implementation"), implementation)
    compiler = "{}: {}".format(red("compiler"), compiler)

    os_ = "{}: {}".format(red("os"), os_ + SPACE + uname.machine)
    kernel = "{}: {}".format(red("kernel"), platform.platform())
    cpu = "{}: {}".format(red("cpu"), get_processor_name().strip())
    ram = "{0}: {1}{3} / {2}{3}".format(red("ram"), mem_used, mem_total, "MiB")

    bright_colors = [color + "███" for color in B_COLORS]
    dark_colors = [color + "███" for color in D_COLORS]

    render(
        [
            SPACE,
            userinfo,
            splitline,
            python_ver,
            pip_ver,
            pip_packages,
            implementation,
            compiler,
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
