#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from setuptools import setup


with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="libmineshaft",
    version="0.1.5",
    description="Helper library for Mineshaft and mod creation for it",
    long_description=long_description,
    author="Double Fractal Game Studios",
    author_email="mayu2kura1@gmail.com",
    maintainer="Alexey Pavlov",
    maintainer_email="pezleha@gmail.om",
    url="http://mineshaft.ml",
    download_url="http://github.com/Mineshaft-game/libmineshaft",
    classifiers=[
        "License :: OSI Approved :: GNU Lesser General Public License v2 or later (LGPLv2+)",
        "Environment :: Console",
        "Intended Audience :: Developers",
        "Natural Language :: English",
        "Operating System :: MacOS",
        "Operating System :: MacOS :: MacOS 9",
        "Operating System :: MacOS :: MacOS X",
        "Operating System :: Microsoft :: Windows",
        "Operating System :: Microsoft :: Windows :: Windows 10",
        "Operating System :: Microsoft :: Windows :: Windows 7",
        "Operating System :: Microsoft :: Windows :: Windows 8",
        "Operating System :: Microsoft :: Windows :: Windows 8.1",
        "Operating System :: OS Independent",
        "Operating System :: POSIX",
        "Operating System :: POSIX :: Linux",
        "Operating System :: Unix",
        "Programming Language :: Other",
        "Programming Language :: Other Scripting Engines",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3 :: Only",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Topic :: Games/Entertainment",
        "Topic :: Games/Entertainment :: Simulation",
        "Topic :: Software Development :: Build Tools",
        "Topic :: Software Development :: Interpreters",
        "Topic :: Software Development :: Libraries :: pygame",
        "Topic :: System :: Shells",
        "Topic :: System :: Software Distribution",
    ],
    keywords=[
        "Minecraft",
        "Mineshaft",
        "Pygame",
        "Minecraft clone",
        "2D",
        "Minecraft 2D",
        "Mineshaft 2D",
        "Minecraft remake",
        "libmineshaft",
        "Minecraft mod",
        "mod",
    ],
    packages=["libmineshaft"],
    install_requires=["pygame>=2.0.1", "pygame-menu"],
    entry_points={
        "console_scripts": [
            "libmineshaft-console = libmineshaft.__main__:main",
            "libms-console = libmineshaft.__main__:main",
            "ms-console = libmineshaft.__main__:main",
        ]
    },
)
