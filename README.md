# pythonfetch

![](https://img.shields.io/badge/python-3.5%2B-blue)
![](https://img.shields.io/pypi/v/pythonfetch)
![](https://img.shields.io/pypi/l/pythonfetch)
![](https://img.shields.io/pypi/dm/pythonfetch)
![](https://img.shields.io/badge/style-black-black)

Python and system information command-line tool

![2022-02-07_22-19](https://user-images.githubusercontent.com/40023234/152856842-565e45c2-15f5-4cea-95d4-8056373e89e5.png)

### Availability
Only GNU/Linux 🐧

## Installation and Building

Install via `pip` (No auto-update):
```
$ pip3 install --user pythonfetch
```

### Building the sources
1. Clone the reporistrory:
```
$ git clone https://github.com/beucismis/pythonfetch
$ cd pythonfetch/
```
2. Create a virtual environment (Optionally):
```
$ virtualenv .venv
$ source .venv/bin/activate
```
3. Install the pythonfetch's dependencies:
```
$ pip3 install -r requirements.txt
```
4. Run build and install:
```
$ python3 setup.py build
$ python3 setup.py install
```

## Usage
```
$ pythonfetch
# or
$ pyfetch
```

## License
This project is licensed under the GPL-3.0 - see the [LICENSE](LICENSE) file for details.
