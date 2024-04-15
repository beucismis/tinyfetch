import sys
import csv
import getpass
import os
import platform
from dataclasses import dataclass, field
from enum import Enum
from pathlib import Path
from typing import Union

BOLD = "\u001b[1m"
RESET = "\u001b[0m"


class Color(Enum):
    red = "\u001b[31m"
    green = "\u001b[32m"
    yellow = "\u001b[33m"
    blue = "\u001b[34m"
    magenta = "\u001b[35m"
    cyan = "\u001b[36m"


@dataclass
class Module:
    title: Union[str, None] = field(init=False, default=None)
    value: str = field(init=False)
    title_color: str = field(default=Color["blue"])
    no_color: bool = field(default=False)

    def output(self) -> str:
        if self.title is None:
            return self.value
        if self.no_color:
            return f"{self.title}: {self.value}"
        return f"{BOLD}{self.title_color.value}{self.title}:{RESET} {self.value}"


@dataclass
class Space(Module):
    def __post_init__(self):
        self.value = ""


@dataclass
class UserHost(Module):
    def __post_init__(self):
        user = getpass.getuser()
        host = os.uname().nodename
        self.userhost = f"{user}@{host}"

        if self.no_color:
            self.value = self.userhost
        else:
            self.value = f"{BOLD}{self.title_color.value}{self.userhost}{RESET}"

    def __len__(self) -> int:
        return len(self.userhost)


@dataclass
class SplitLine(Module):
    char: str = field(init=False, default="-")

    def __post_init__(self):
        userhost = UserHost()
        self.value = len(userhost) * self.char


@dataclass
class PythonVersion(Module):
    def __post_init__(self):
        self.title = "Python Version"
        self.value = platform.python_version()


@dataclass
class PIPVersion(Module):
    def __post_init__(self):
        from pip import __version__

        self.title = "PIP Version"
        self.value = __version__


@dataclass
class PIPPackages(Module):
    def __post_init__(self):
        from pip._internal.operations.freeze import freeze

        self.title = "PIP Packages"
        self.value = len(list(freeze(local_only=True)))


@dataclass
class Implementation(Module):
    def __post_init__(self):
        self.title = self.__class__.__name__
        self.value = platform.python_implementation()


@dataclass
class Compiler(Module):
    def __post_init__(self):
        self.title = self.__class__.__name__
        self.value = platform.python_compiler()


@dataclass
class Kernel(Module):
    def __post_init__(self):
        self.title = self.__class__.__name__
        self.value = f"{os.uname().sysname}-{os.uname().release}"


@dataclass
class OperationSystem(Module):
    def __post_init__(self):
        self.title = "OS"
        platform_type = self.get_platform()

        if platform_type == "linux":
            self.value = self.get_linux_os_name()
        if platform_type == "android":
            self.value = "Android"
        if platform_type == "unknown":
            self.value = "Unkown"

    def get_platform(self):
        if "P4A_BOOTSTRAP" in os.environ:
            return "android"
        if "ANDROID_ARGUMENT" in os.environ:
            return "android"
        if sys.platform in ("win32", "cygwin"):
            return "win"
        if sys.platform == "darwin":
            return "macosx"
        if sys.platform.startswith("linux"):
            return 'linux'
        if sys.platform.startswith("freebsd"):
            return "linux"
        return "unknown"

    def get_linux_os_name(self) -> str:
        path = Path("/etc/os-release")
        with open(path) as file:
            reader = csv.reader(file, delimiter="=")
            return dict(reader)["PRETTY_NAME"] + " " + os.uname().machine