# dds2024_estellelouineau

[![PyPI](https://img.shields.io/pypi/v/dds2024_estellelouineau.svg)][pypi status]
[![Status](https://img.shields.io/pypi/status/dds2024_estellelouineau.svg)][pypi status]
[![Python Version](https://img.shields.io/pypi/pyversions/dds2024_estellelouineau)][pypi status]
[![License](https://img.shields.io/pypi/l/dds2024_estellelouineau)][license]

[![Read the documentation at https://dds2024_estellelouineau.readthedocs.io/](https://img.shields.io/readthedocs/dds2024_estellelouineau/latest.svg?label=Read%20the%20Docs)][read the docs]
[![Tests](https://github.com/estellelouineau/dds2024_estellelouineau/actions/workflows/python-test.yml/badge.svg)][tests]
[![Codecov](https://codecov.io/gh/estellelouineau/dds2024_estellelouineau/branch/main/graph/badge.svg)][codecov]

[![pre-commit](https://img.shields.io/badge/pre--commit-enabled-brightgreen?logo=pre-commit&logoColor=white)][pre-commit]
[![Black](https://img.shields.io/badge/code%20style-black-000000.svg)][black]

[pypi status]: https://pypi.org/project/dds2024_estellelouineau/
[read the docs]: https://dds2024_estellelouineau.readthedocs.io/
[tests]: https://github.com/estellelouineau/dds2024_estellelouineau/actions?workflow=Tests
[codecov]: https://app.codecov.io/gh/estellelouineau/dds2024_estellelouineau
[pre-commit]: https://github.com/pre-commit/pre-commit
[black]: https://github.com/psf/black

## Installation

You can install _kartoffel_ via [pip] from [PyPI]:

```console
$ pip install kartoffel
```

## Contributing

Contributions are very welcome.
To learn more, see the [Contributor Guide][Contributor Guide].

## License

Distributed under the terms of the [MIT license][License],
_kartoffel_ is free and open source software.

## Issues

If you encounter any problems,
please [file an issue][Issue Tracker] along with a detailed description.


<!-- github-only -->

[command-line reference]: https://dds2024_estellelouineau.readthedocs.io/en/latest/usage.html
[License]: https://github.com/estellelouineau/dds2024_estellelouineau/blob/main/LICENSE
[Contributor Guide]: https://github.com/estellelouineau/dds2024_estellelouineau/blob/main/CONTRIBUTING.md
[Issue Tracker]: https://github.com/estellelouineau/dds2024_estellelouineau/issues


## Building the Documentation

You can build the documentation locally by installing the documentation Conda environment:

```bash
conda env create -f docs/environment.yml
```

activating the environment

```bash
conda activate sphinx_dds2024_estellelouineau
```

and [running the build command](https://www.sphinx-doc.org/en/master/man/sphinx-build.html#sphinx-build):

```bash
sphinx-build docs _build/html --builder=singlehtml --jobs=auto --write-all; open _build/html/index.html
```