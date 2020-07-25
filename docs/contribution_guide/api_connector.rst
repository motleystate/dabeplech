*************
API connector
*************

New API = New Module
====================

When adding a new API connector, please create a new module within ``dabeplech`` with
the api name. (e.g. ``dabeplech/myawesomeapi.py``).

.. note::
    To ease import while using ``dabeplech``, do not forget to import your new classes
    to ``dabeplech/__init__.py``.

Creating your API connector
===========================

Base Structure
--------------

All API connectors try to follow the same structure and therefore has to inherit from
``dabeplech.base.BaseAPI``.

Here is the structure of the class:

.. autoclass:: dabeplech.base.BaseAPI
    :members:
    :undoc-members:
    :show-inheritance:

When adding a new API connector, you inherit from the ``BaseAPI`` class and then overload ``BASE_URL``
with the base ``url`` of your API. From this new class you can create as many child
classes as routes the API provides and overload ``ROUTE`` class attribute.

Then, you need to add methods to perform requests (``GET``, ``POST``...) and the approach
will depend on the API your are adding:

- :ref:`contrib_api`
- :ref:`contrib_api_parser`

Example
'''''''

Let's say we want to add our new awesome API which has ``https://awesomebioinfo.com/``
as base url and contains two routes:

- ``https://awesomebioinfo.com/genes``: obtain information about genes
- ``https://awesomebioinfo.com/organisms``: obtain information about organisms

Here is the code that we write to add this API in ``dabeplech/awesomebioinfo.py`` file:

.. code-block:: python

    from dabeplech.base import BaseAPI

    class AwesomebioinfoAPI(BaseAPI):
        BASE_URL = "https://awesomebioinfo.com/"

    class AwesomebioinfoGenesAPI(AwesomebioinfoAPI):
        ROUTE = "genes/"

    class AwesomebioinfoOrganismsAPI(AwesomebioinfoAPI):
        ROUTE = "organisms/"

.. warning::
    As it is, your connectors won't work since no methods are defined to perform
    requests. This question is adressed below.

.. _contrib_api:

Once this module has been created, add it to the ``dabeplech/__init__.py`` file so that it can be imported.
In this case, the code added at the bottom of this file would be:

.. code-block:: python

    from .awesomebioinfo import ( #noqa
        AwesomebioinfoAPI,
        AwesomebioinfoGenesAPI,
        AwesomebioinfoOrganismsAPI,
    )

Adding an API returning JSON
----------------------------

A list of Mixins is available to build your API connectors. You just need to perform multiple
inheritance for your new classes with the corresponding Mixins to add the methods.
Here is a description of the different Mixins:

.. autoclass:: dabeplech.base.LISTMixin
    :members:
    :undoc-members:
    :show-inheritance:

.. autoclass:: dabeplech.base.GETMixin
    :members:
    :undoc-members:
    :show-inheritance:

.. autoclass:: dabeplech.base.POSTMixin
    :members:
    :undoc-members:
    :show-inheritance:

.. autoclass:: dabeplech.base.PUTMixin
    :members:
    :undoc-members:
    :show-inheritance:

Example
'''''''

From the previous example, we consider the two endpoints allow to obtain list of genes
and organisms, but also retrieve an item based on its ID. The code becomes:

.. code-block:: python

    from dabeplech.base import BaseAPI, LISTMixin, GETMixin

    class AwesomebioinfoAPI(BaseAPI, LISTMixin, GETMixin):
        BASE_URL = "https://awesomebioinfo.com/"

    class AwesomebioinfoGenesAPI(AwesomebioinfoAPI):
        ROUTE = "genes/"

    class AwesomebioinfoOrganismsAPI(AwesomebioinfoAPI):
        ROUTE = "organisms/"

Now you can use your api connector (considering classes are added to ``dabeplech/__init__.py``):

.. code-block:: python

    from dabeplech import AwesomebioinfoGenesAPI

    api = AwesomebioinfoGenesAPI()

    # Get all genes
    all_genes = api.get_all()
    # Get one gene with its ID
    the_gene = api.get('my-fav-gene')

.. _contrib_api_parser:

Adding an API based on a Parser
-------------------------------

There is not automatic way to help you use your parsers while adding an API connector using a
parser to structure the response into JSON.

At the moment, please refer to the ``dabeplech.kegg`` module for examples using parsers.

.. Note::
    An more abstracted way of dealing with parser will be extracted in the future when needed.
    The Kegg case being particular, it needs its own methods.
