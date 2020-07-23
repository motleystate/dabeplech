.. _contrib_parser:

*******
Parsers
*******

.. Warning::
    This step is optional and is required only if the related API does not return
    JSON format.

Some API does not follow any standard and it can be complex to deal with its content.
Thus, you might need to build some parsers to make the response stick to the model
you described for the API

Parser structure
================

Parsers are build on the :ref:`model previously described <contrib_model>` for your API.
An abstract class is available to give you the main lines to build your parser:

.. automodule:: dabeplech.parsers.base
    :members:
    :undoc-members:
    :special-members: __init__
    :show-inheritance:

.. Note::
    We are aware that some API needs more specific and complex parsing, but the idea
    is to be perform parsing with the ``parse`` method and obtain the validated
    data with ``validated_entry`` property.

Test your parser
================

You can add your unit tests for your parser within ``/tests/dabeplech/parsers`` directory.
You can have a look at the tests for kegg to help you build your own tests.