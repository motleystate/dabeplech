Welcome to dabeplech's documentation!
=====================================

dabeplech is a modern and light library to perform requests to different bioinformatics APIs with Python 3.6+.
The key features of the library are the following:

- **Accessible**: Designed to be easy to use.
- **Open**: Easy to contribute to and add modules to deal with your own API.
- **Standards-based**: Based on OpenAPI, the open standards for APIs.

Quickstart
----------

Installation
""""""""""""

.. code-block:: bash

   pip install dabeplech

Example
"""""""

.. code-block:: python

   from dabeplech import KEGGAPI

   api = KEGGAPI()
   kegg_entry = api.get("K00135")

   print(kegg_entry.names)
   # OUTPUT: ['gabD']


---------------

.. toctree::
    :caption: Dabeplech
    :maxdepth: 1

    why_dabeplech
    contribution_guide/contributing

.. toctree::
    :caption: User guide
    :maxdepth: 2

    user_guide/installation
    user_guide/basic_usage
    user_guide/supported_api
    user_guide/scrapped_pages

.. toctree::
    :caption: Contribution guide
    :maxdepth: 1

    contribution_guide/environment
    contribution_guide/flow
    contribution_guide/model
    contribution_guide/parser
    contribution_guide/scrapper
    contribution_guide/api_connector
    contribution_guide/docs
    contribution_guide/code_of_conduct

.. toctree::
    :caption: API Documentation
    :maxdepth: 1

    api_docs/api_services
    api_docs/scrap_api
    api_docs/parsers
    api_docs/scrappers

.. toctree::
    :caption: Changelogs
    :maxdepth: 1

    changelogs

..
  Indices and tables
  ==================

  * :ref:`genindex`
  * :ref:`modindex`
  * :ref:`search`
