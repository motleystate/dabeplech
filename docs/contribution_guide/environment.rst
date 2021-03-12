.. _contrib_environment:

***********************
Development environment
***********************

This page contains some guidelines to set up your environment to contribute to the project.

Install package for development
===============================

Packaging and organization of the library is done using Poetry_

.. _Poetry: https://python-poetry.org/docs/

.. code-block:: bash

    poetry install

This will install both dependencies needed for the library and for the development of the library.

Quality and tests
=================

Quality and tests can be run using tasks. To obtain the full list:

.. code-block:: bash

    poetry run inv --list

Quality
-------

Code is formated using Black_. To run it:

.. code-block:: bash

    poetry run inv quality.black-format

Documentation style is checked using pydocstyle_. To run it:

.. code-block:: bash

    poetry run inv quality.docstyle

Finally linting is done with Flake8_. To run it:

.. code-block:: bash

poetry run inv quality.lint

.. _Black: https://black.readthedocs.io/en/stable/
.. _pydocstyle: http://www.pydocstyle.org/en/stable/
.. _Flake8: https://flake8.pycqa.org/en/latest/

Unit tests
----------

To run all the unit tests you can use the following command from the root of the project:

.. code-block:: bash

    poetry run inv tests.unit

.. Note::

    ``-s`` and ``-v`` options are used to get more details about the tests and redirect all output to stdout.

You can also only run selected tests by specifying the name of the test file:

.. code-block:: bash

    poetry run pytest -s -v tests/dabeplech/parsers/

.. Note::

    You can find more information in the pytest_ documentation.

.. _pytest: https://docs.pytest.org/en/stable/kegg/test_orthology.py