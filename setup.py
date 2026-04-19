from setuptools import setup, find_packages

setup(
    name="keylogger",
    version="1.0",
    packages=find_packages(),
    install_requires=[
        "pyhook",
        "requests",
    ],
    entry_points={
        "console_scripts": [
            "keylogger=keylogger:main",
        ],
    },
)
