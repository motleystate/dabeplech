.. _contrib_model:

*********************************
Model description of the response
*********************************

.. Warning::
    This step is optional and is required only if the related API does not return
    JSON format. Its main purpose at the moment is to help you build parsers.

Models description are done using pydantic_. In brief, it uses Python type
annotations to perform validations. Please check to
`Pydantic models documentation <https://pydantic-docs.helpmanual.io/usage/models/>`_
for more details.

.. Note::
    This step is done manually at the moment, but we could imagine using or creating
    a tool that generates, in a semi-automatic manner the base structure for the
    response based on a openapi specification.

All the models are present in the ``models`` module of the bioapi library.

Describing your response should be pretty straightforward and is only a matter
of defining the structure of it. Let's have a look at a simple example.

Example
=======

Let's say your API return some information about a gene:

.. code-block:: yaml

    {
        'gene_id': 'gene-3529',
        'name': 'Illestere',
        'sequence': 'acgtatcgaacagcatgcatgt'
    }

You could therefore describe your response as followed:

.. code-block:: python

    from pydantic import BaseModel

    class GeneModel(BaseModel):
        gene_id: str
        name: str
        sequence: str

It is as simple as that!

.. Note::
    Structure can be way more complex, with nested structure, regex validation, non mandatory
    fields... You can find all you need on the
    `Pydantic models documentation <https://pydantic-docs.helpmanual.io/usage/models/>`_.

.. _pydantic: https://github.com/samuelcolvin/pydantic/