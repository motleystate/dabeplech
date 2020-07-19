***********
Basic usage
***********

Get data with API connectors
============================

KEGG example
------------

Get results (as a Pydantic model):
__________________________________

By default, the result is returned using the pydantic model.

.. code-block:: python

   from bioapi import KEGGAPI

   api = KEGGAPI()
   kegg_entry = api.get("K00135")

   print(kegg_entry.names)
   # OUTPUT: ['gabD']

Get results as a Python dict:
_____________________________

If you prefer you can instead get a python dict with the ``get_model=False`` argument.

.. code-block:: python

   from bioapi import KEGGAPI

   api = KEGGAPI()
   kegg_entry = api.get("K00135", get_model=False)

   print(kegg_entry.get('names'))
   # OUTPUT: ['gabD']

.. Note::
  You can also directly retrieve a dict from the model using ``.dict()`` method.
