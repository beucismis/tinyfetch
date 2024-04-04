import getpass
import os
import platform
import re
from dataclasses import dataclass, field
from enum import Enum
from pathlib import Path

from pip import __version__ as pip__version__
from pip._internal.operations.freeze import freeze


@dataclass
class Module:
    title: str = field(init=False, default=None)
    value: str = field(init=False)

    def output(self):
        if self.title is None:
            return self.value
        return f"{self.title}: {self.value}"


@dataclass
class UserHost(Module):
    def __post_init__(self):
        user = getpass.getuser()
        host = os.uname().nodename
        self.value = f"{user}@{host}"

    def __len__(self):
        return len(self.value)


@dataclass
class SplitLine(Module):
    userhost: UserHost
    char: str = field(init=False, default="-")

    def __post_init__(self):
        self.value = len(self.userhost) * self.char


@dataclass
class PythonVersion(Module):
    def __post_init__(self):
        self.title = "Python Version"
        self.value = platform.python_version()


@dataclass
class PIPVersion(Module):
    def __post_init__(self):
        self.title = "PIP Version"
        self.value = pip__version__


@dataclass
class PIPPackages(Module):
    def __post_init__(self):
        self.title = "PIP Packages"
        self.value = sum(1 for p in freeze(local_only=True))


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
        uname = os.uname()
        self.value = f"{uname.sysname}-{uname.release}"


@dataclass
class OperationSystem(Module):
    def __post_init__(self):
        self.title = "OS"
        uname = os.uname()
        if os.name == "posix":
            self.value = self.posix_os_name() + " " + uname.machine

    def posix_os_name(self):
        pretty_name = re.compile('^PRETTY_NAME="([^"]+)"$')
        for p in Path("/").glob("etc/*release"):
            with p.open() as file:
                match = [pretty_name.match(l) for l in file.readlines()][0]
            if match:
                return match.group(1) if match.group(1) != "" or None else " "
