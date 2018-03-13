#!/usr/bin/env python
from setuptools import setup, find_packages
from codecs import open
from os import path
import pypandoc

here = path.abspath(path.dirname(__file__))
with open(path.join(here, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

setup(
    name="h5nav",
    version="0.1.1",
    packages=find_packages(exclude=['docs']),
    entry_points={
        'console_scripts': [
            'h5nav = h5nav.cli:main',
        ],
    },

    install_requires=[
        'numpy>=1.10',
        'h5py>=2.5',
        'future>=0.16.0',
    ],

    # metadata
    author="Corentin J. Lapeyre",
    author_email="corentin.lapeyre@gmail.com",
    description="hdf5 file interactive navigation and editing tool",
    long_description=long_description,
    license="MIT",
    url="https://github.com/clapeyre/h5nav",
    classifiers=[
        'Development Status :: 3 - Alpha',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
    ],
    keywords='h5py interactive',
    project_urls={
        'Say Thanks!': 'http://saythanks.io/to/example',
        'Source': "https://github.com/clapeyre/h5nav",
    },
)

z = pypandoc.convert('README.md', 'rst', format='markdown').encode('utf-8')
with open('README.rst','w') as outfile:
    outfile.write(z)
