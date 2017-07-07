#!/usr/bin/env python
from setuptools import setup, find_packages

setup(
    name="h5nav",
    version="0.1.0",
    packages=find_packages(),
    # scripts=['flametransfer/flametransfer.py'],
    entry_points={
        'console_scripts': [
            'h5nav = h5nav.cli:main',
        ],
    },

    install_requires=[
        'numpy>=1.10',
        'h5py>=2.5',
    ],

    # metadata
    author="Corentin J. Lapeyre",
    author_email="lapeyre@cerfacs.fr",
    description="hdf5 file interactive navigation tool",
    license="MIT",
    url="https://github.com/clapeyre/h5nav",
)
