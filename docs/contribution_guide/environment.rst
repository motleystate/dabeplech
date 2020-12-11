.. _contrib_environment:

***********************
Development environment
***********************

This page contains some guidelines to set up your environment to contribute to the project.

Virtual environment with ``venv``
=================================

.. code-block:: bash

    python3 -m venv dabeplech_env
    source ./dabeplech_env/bin/activate

This creates a directory ``./dabeplech_env/`` with the Python binaries you used. You can now use the independant environment
to install the project and packages.

.. Note::
    Once activated, you can check it worked using ``which pip`` commands for instance.

Install development dependencies
================================

The list of tools that are only used during the development process of the library are listed in ``requirements-dev.txt`` file.

.. code-block:: bash

    pip install -r requirements-dev.txt

Quality and tests
=================

You can run all quality steps and unit tests locally using the ``run_local_quality_tests.sh`` script.

Here is a detail of the different steps.

Quality
-------

Code is formated using Black_. To run it:

.. code-block:: bash

    black dabeplech/

Documentation style is checked using pydocstyle_. To run it:

.. code-block:: bash

    pydocstyle dabeplech/

Finally linting is done with Flake8_. To run it:

.. code-block:: bash

    flake8 --max-complexity=10 --max-line-length=127 dabeplech/

.. _Black: https://black.readthedocs.io/en/stable/
.. _pydocstyle: http://www.pydocstyle.org/en/stable/
.. _Flake8: https://flake8.pycqa.org/en/latest/

Unit tests
----------

To run all the unit tests you can use the following command from the root of the project:

.. code-block:: bash

    pytest -s -v

.. Note::

    ``-s`` and ``-v`` options are used to get more details about the tests and redirect all output to stdout.

You can also only run selected tests by specifying the name of the test file:

.. code-block:: bash

    pytest -s -v tests/dabeplech/parsers/

.. Note::

    You can find more information in the pytest_ documentation.

.. _pytest: https://docs.pytest.org/en/stable/kegg/test_orthology.py