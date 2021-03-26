# dabeplech

![Python package](https://github.com/motleystate/dabeplech/workflows/Python%20package/badge.svg)
[![codecov](https://codecov.io/gh/motleystate/dabeplech/branch/master/graph/badge.svg)](https://codecov.io/gh/motleystate/dabeplech)
[![Documentation Status](https://readthedocs.org/projects/dabeplech/badge/?version=latest)](https://dabeplech.readthedocs.io/en/latest/?badge=latest)
[![Downloads](https://pepy.tech/badge/dabeplech)](https://pepy.tech/project/dabeplech)

Light library to perform requests to different bioinformatics APIs.
This library also contains models description (thanks to [pydantic](https://github.com/samuelcolvin/pydantic/)). It allows automatic
documentation of the responses from API that are initially not described.

Please have a look at our [Documentation](https://dabeplech.readthedocs.io/en/latest/index.html) for more information.

#### List of supported services

List of supported services is listed in the [documentation](https://dabeplech.readthedocs.io/en/latest/user_guide/supported_api.html).

## Install

Latest published version:

```python
pip install dabeplech
```

## Basic usage

```python
from dabeplech import KEGGAPI

api = KEGGAPI()
kegg_entry = api.get("K00135")
print(kegg_entry.names)
# OUTPUT: ['gabD']
```

-----------------------------------------

### Test endpoints

Status of different endpoints can be test with `api_status.py` script from `tests` directory.

If the test works, you will get some green output. Do not be surprised if you get `ERROR` in green, it means it is expected.

-----------------------------------------

# Development

Packaging and organization of the library is done using [Poetry](https://python-poetry.org/docs/).

In brief after [installing](https://python-poetry.org/docs/#installation) poetry, from the repository
directory, just run:

```bash
poetry install
```

## Run all quality checks and tests locally

You can run all quality checks and unit tests locally.

To list all available commands:

```bash
poetry run inv --list
# for instance
poetry run inv quality.all  # Run all quality tests
```

-----------------------------------------

## Contributions

All contributions are welcome. Please have a look at our [Contribution Guide](https://dabeplech.readthedocs.io/en/latest/contribution_guide/contributing.html).
