# h5nav

[![Coverage
Status](https://coveralls.io/repos/github/clapeyre/h5nav/badge.svg?branch=master)](https://coveralls.io/github/clapeyre/h5nav?branch=master)
![python](https://img.shields.io/badge/python-2.7-blue.svg)
![release](https://img.shields.io/badge/release-v0.1.0-blue.svg)
[![Say Thanks!](https://img.shields.io/badge/Say%20Thanks-!-1EAEDB.svg)](https://saythanks.io/to/corentin.lapeyre%40gmail.com)

Python tool for interactive navigation of an hdf5 file in a "unix shell"
fashion.

## Installation

Whether for python 2 or 3, it's as simple as:

    pip install h5nav

## Contributing

To install locally, start by getting the files:

    git clone https://github.com/clapeyre/h5nav.git

Make sure you have `pandoc` installed, as it is used to convert the `README.md`
to `README.rst` file. The first is the source, used on GitHub. The latter is
generated, so as to show up on PyPI. Then, run:

    make develop

in your favorite (virtual) environment. You are ready to work in h5nav, and see
your work dynamically updated when calling `h5nav`. Please submit merge
requests directly on GitHub.

## Authors

* [**Corentin J. Lapeyre**](https://clapeyre.github.io/)
