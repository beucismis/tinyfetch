# tinyfetch

![PyPI - Python Version](https://img.shields.io/pypi/pyversions/tinyfetch)
![PyPI - Version](https://img.shields.io/pypi/v/tinyfetch)
![GitHub License](https://img.shields.io/github/license/beucismis/tinyfetch)
![GitHub Actions Workflow Status](https://img.shields.io/github/actions/workflow/status/beucismis/tinyfetch/test.yml?label=test)
![GitHub Actions Workflow Status](https://img.shields.io/github/actions/workflow/status/beucismis/tinyfetch/publish.yml?label=publish)

Python and system information command-line fetch tool.

```
$ tinyfetch

     ___     beucismis@thinkpad-devuan
    (.. \    -------------------------
    (<> |    Python Version: 3.11.2
   //  \ \   PIP Version: 24.0
  ( |  | /|  PIP Packages: 341
 _/\ __)/_)  Implementation: CPython
 \/-____\/   Compiler: GCC 12.2.0

             Kernel: Linux-6.1.0-18-amd64
             OS: Devuan GNU/Linux 5 (daedalus) x86_64
```

Output like this! Also, tux ASCII logo is inspired by [fastfetch](https://github.com/fastfetch-cli/fastfetch). Thanks!

## Installation

```
pip install -U tinyfetch
```

## Documentation

```
$ tinyfetch --help

usage: tinyfetch [-h] [--title-color {red,green,yellow,blue,magenta,cyan,white}] [--no-color] [--version]

Python and system information command-line fetch tool

options:
  -h, --help            show this help message and exit
  --title-color {red,green,yellow,blue,magenta,cyan,white}
                        set default the title color
  --no-color            turn off all colors and disables
  --version             show program's version number and exit
```

## License

`tinyfetch` is distributed under the terms of the [MIT](LICENSE.txt) license.
