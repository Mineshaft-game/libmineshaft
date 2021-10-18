from setuptools import setup

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()


setup(
    name='libmineshaft',
    version='0.1.1a',
    description='Helper library for Mineshaft and mod creation for it in near future',
    url='https://github.com/Mineshaft-game/libmineshaft',
    author='Double Fractal Game Studios',
    author_email='mayu2kura1@gmail.com',
    license='LGPL-2.1',
    long_description=long_description,
    long_description_content_type="text/markdown",
    packages=['libmineshaft'],
    install_requires=[
                      'pygame>=2.0.1',
                      ],

    classifiers=[
        'Development Status :: 1 - Planning',
        'Programming Language :: Python :: 3',
    ],
)
