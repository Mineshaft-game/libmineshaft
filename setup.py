from setuptools import setup

setup(
    name='libmineshaft',
    version='0.1.0',
    description='Helper library for Mineshaft and mod creation for it',
    url='https://github.com/Mineshaft-game/libmineshaft',
    author='Double Fractal Game Studios',
    author_email='mayu2kura1@gmail.com',
    license='LGPL-2.1',
    packages=['libmineshaft'],
    install_requires=[
                      'pygame>=2.0.1',
                      ],

    classifiers=[
        'Development Status :: 1 - Planning',
        'Programming Language :: Python :: 3',
    ],
)
