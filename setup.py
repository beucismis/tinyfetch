import sys
import setuptools
import pythonfetch as pf
from os import name as os_name


if os_name != "posix" or "nt":
    raise OSError(f"Unsported OS: {os_name}")

if sys.version_info < (3, 5):
    raise RuntimeError("pythonfetch requires Python 3.5 or later")

with open("README.md") as f:
    long_description = f.read()


setuptools.setup(
    name="pythonfetch",
    packages=["pythonfetch"],
    version=pf.__version__,
    description=pf.__description__,
    long_description=long_description,
    long_description_content_type="text/markdown",
    url=pf.__source__,
    author=pf.__author__,
    author_email=pf.__contact__,
    license=pf.__license__,
    classifiers=[
        "Natural Language :: English",
        "Environment :: Console",
        "Operating System :: POSIX :: Linux",
        "Intended Audience :: Developers",
        "Intended Audience :: End Users/Desktop",
        "Programming Language :: Python :: 3.5",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Topic :: Software Development :: Version Control",
    ],
    platforms=["Linux"],
    python_requires=">=3.5",
    keywords=["pyfetch pythonfetch information command-line tool"],
    entry_points={
        "console_scripts": [
            "pyfetch = pythonfetch:main",
            "pythonfetch = pythonfetch:main",
        ],
    },
)
