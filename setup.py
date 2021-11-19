from setuptools import setup

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()


setup(
    name="libmineshaft",
    version="0.1.5",
    description="Helper library for Mineshaft and mod creation for it in near future",
    url="https://github.com/Mineshaft-game/libmineshaft",
    author="Double Fractal Game Studios",
    author_email="mayu2kura1@gmail.com",
    license="LGPL-2.1",
    long_description=long_description,
    long_description_content_type="text/markdown",
    packages=["libmineshaft"],
    install_requires=["pygame>=2.0.1", "pygame-menu"],
    classifiers=[
        "Development Status :: 2 - Pre-Alpha",
        "Programming Language :: Python :: 3",
        "Operating System :: OS Independent",
        "Intended Audience :: Developers",
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
    entry_points = {
        "console_scripts" : [
            "libmineshaft-console = libmineshaft.__main__:main", 
            "libms-console = libmineshaft.__main__:main", 
            "ms-console = libmineshaft.__main__:main", 
        ], 
    }, 
)
