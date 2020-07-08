.. _contrib_environment:

***********************
Development environment
***********************

This page contains some guidelines to set up your environment to contribute to the project.

Virtual environment with ``venv``
=================================

.. code-block:: bash

    python3 -m venv bioapi_env
    source ./bioapi_env/bin/activate

This creates a directory ``./bioapi_env/`` with the Python binaries you used. You can now use the independant environment
to install the project and packages.

.. Note::
    Once activated, you can check it worked using ``which pip`` commands for instance.

Install development dependencies
================================

The list of tools that are only used during the development process of the library are listed in ``requirements-dev.txt`` file.

.. code-block:: bash

    pip install -r requirements-dev.txt

Linting
=======

The BioAPI project uses Flake8_ in its continuous integration process to check the code style and structure.

.. _Flake8: https://flake8.pycqa.org/en/latest/

You can reuse the commands at the root of the project in your environment to check the syntax and structure of your code.

First, it stops the build if there are Python syntax errors or undefined names:

.. code-block:: bash

    flake8 . --count --select=E9,F63,F7,F82 --show-source --statistics

Then, exit-zero treats all errors as warnings and the maximum number of character per line is set to 127.

.. code-block:: bash

    flake8 . --count --exit-zero --max-complexity=10 --max-line-length=127 --statistics

.. Note::

    The two commands are suggested by Github actions while setting up some CI.

Unit tests
==========

To run all the unit tests you can use the following command from the root of the project:

.. code-block:: bash

    pytest -s -v

.. Note::

    ``-s`` and ``-v`` options are used to get more details about the tests and redirect all output to stdout.

You can also only run selected tests by specifying the name of the test file:

.. code-block:: bash

    pytest -s -v tests/bioapi/parsers/

.. Note::

    You can find more information in the pytest_ documentation.

.. _pytest: https://docs.pytest.org/en/stable/kegg/test_orthology.py