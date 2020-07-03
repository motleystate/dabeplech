Welcome to BioAPI's documentation!
==================================

BioAPI is a modern and light library to perform requests to different bioinformatics APIs with Python 3.6+.
The key features of the library are the following:

- **Accessible**: Designed to be easy to use.
- **Open**: Easy to contribute to and add modules to deal with your own API.
- **Standards-based**: Based on OpenAPI, the open standards for APIs.

Quickstart
----------

Installation
""""""""""""

.. code-block:: bash

   pip install bioapi

Example
"""""""

.. code-block:: python

   from bioapi import KEGGAPI

   api = KEGGAPI()
   kegg_entry = api.get("K00135")

   print(kegg_entry.get('name'))
   # OUTPUT: gabD


---------------

.. toctree::
    :caption: BioAPI
    :maxdepth: 2

    why_bioapi
    contribution_guide

.. toctree::
    :caption: User guide
    :maxdepth: 2

    installation
    basic_usage
    supported_api

.. toctree::
    :caption: API Documentation
    :maxdepth: 1

    API_doc

Changelogs
==========
.. toctree::
   :maxdepth: 1

   changelog

..
  Indices and tables
  ==================

  * :ref:`genindex`
  * :ref:`modindex`
  * :ref:`search`
