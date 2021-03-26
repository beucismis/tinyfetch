import sys
import setuptools
import pythonfetch as pf
from os import path, name as os_name


setupdir = path.dirname(__file__)

if os_name != "posix":
    raise OSError(f"Unsported OS: {os_name}")

if sys.version_info < (3, 5):
    raise RuntimeError("r2tg_bot requires Python 3.5 or later")

with open(path.join(setupdir, "README.md"), encoding="utf-8") as f:
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
    classifiers=[],
    platforms=["Linux"],
    python_requires=">=3.5",
    install_requires=["psutil", "colorama"],
    keywords=[""],
    package_data={"pythonfetch": ["data/ascii-art.txt", "data/blocks-art.txt"]},
    entry_points={
        "console_scripts": [
            "pythonfetch = pythonfetch:main",
        ],
    },
)
