.. BioAPI

.. _how_to_use:

*******************
How to use BioAPI ?
*******************

Get data with API connectors
============================



KEGG example
------------

Get results as a Python dict:
_____________________________

.. code-block:: python

   from bioapi import KEGGAPI

   api = KEGGAPI()
   kegg_entry = api.get("K00135")

   print(kegg_entry.get('name'))
   # OUTPUT: gabD

Get results as a Pydantic model:
________________________________

.. code-block:: python

   from bioapi import KEGGAPI

   api = KEGGAPI()
   kegg_entry = api.get("K00135", get_model=True)

   print(kegg_entry.name)
   # OUTPUT: gabD
