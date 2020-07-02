.. BioAPI

Welcome to BioAPI's documentation!
==================================

BioAPI is a modern, light library to perform requests to different bioinformatics APIs with Python 3.6+.

The main focusses are:

- **Accessible**: Designed to be easy to use.
- **Open**: Easy to contribute to and  .
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


BioAPI Documentation
====================
.. toctree::
   :maxdepth: 1

   why_bioapi
   installation
   how_to_use
   supported_api
   contribution_guide

BioAPI API Documentation
=========================
.. toctree::
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
