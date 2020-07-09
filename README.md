# Bioapi

![Python package](https://github.com/khillion/bioapi/workflows/Python%20package/badge.svg)
[![codecov](https://codecov.io/gh/khillion/bioapi/branch/master/graph/badge.svg)](https://codecov.io/gh/khillion/bioapi)
[![Documentation Status](https://readthedocs.org/projects/bioapi/badge/?version=latest)](https://bioapi.readthedocs.io/en/latest/?badge=latest)

Light library to perform requests to different bioinformatics APIs.
This library also contains models description (thanks to [pydantic](https://github.com/samuelcolvin/pydantic/)). It allows automatic
documentation of the responses from API that are initially not described.

Please have a look at our [Documentation](https://bioapi.readthedocs.io/en/latest/index.html) for more information.

#### List of supported services

List of supported services is listed in the [documentation](https://bioapi.readthedocs.io/en/latest/user_guide/supported_api.html).

## Install

```python
pip install bioapi
```

## Basic usage

```python
from bioapi import KEGGAPI

api = KEGGAPI()
kegg_entry = api.get("K00135")
```

`kegg_entry` should then be a dictionnary of the information you can get from the KEGG API.

> KEGG API does not return `json` format but instead some `plain text`. A parser is therefore necessary (`bioapi/parsers/kegg`) and `plain text` is returned if no parser is available for the requested database (e.g. pathway, module...)

You can also get the Pydantic model instead of a `dict`:

```python
from bioapi import KEGGAPI

api = KEGGAPI()
kegg_entry = api.get("K00135", get_model=True)
kegg_entry_dict = kegg_entry.dict()  # Transform model to dict
```

-----------------------------------------

### Test endpoints

Status of different endpoints can be test with `api_status.py` script from `tests` directory.

If the test works, you will get some green output. Do not be surprised if you get `ERROR` in green, it means it is expected.

-----------------------------------------

## Contributions

All contributions are welcome. Please have a look at our [Contribution Guide](https://bioapi.readthedocs.io/en/latest/contribution_guide/contributing.html).
