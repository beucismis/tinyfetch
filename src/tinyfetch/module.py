import csv
import getpass
import os
import platform
from dataclasses import dataclass, field
from pathlib import Path

RESET = "\u001b[0m"
BOLD = "\u001b[1m"
MAIN = BOLD + "\u001b[034m"


@dataclass
class Module:
    title: str = field(init=False, default=None)
    value: str = field(init=False)

    def output(self):
        if self.title is None:
            return self.value
        return f"{MAIN}{self.title}:{RESET} {self.value}"


@dataclass
class Space(Module):
    def __post_init__(self):
        self.value = " "


@dataclass
class UserHost(Module):
    def __post_init__(self):
        user = getpass.getuser()
        host = os.uname().nodename
        self.userhost = f"{user}@{host}"
        self.value = MAIN + self.userhost + RESET

    def __len__(self):
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

        if os.name == "posix":
            self.value = self.posix_os_name()

    def posix_os_name(self):
        path = Path("/etc/os-release")
        with open(path) as file:
            reader = csv.reader(file, delimiter="=")
            return dict(reader)["PRETTY_NAME"] + " " + os.uname().machine
