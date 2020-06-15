.. BioAPI

.. _install:

************
Installation
************

Requirements
============

BioAPI works with version of Python >= 3.6.0 and uses the following dependencies:

- pydantic_ (==1.5.1)
- requests (==2.23.0)

.. _pydantic: https://github.com/samuelcolvin/pydantic/

.. Note::
    We highly recommend the use of a virtual environment such as `virtualenv`_ or `conda`_.

.. _virtualenv: https://virtualenv.pypa.io/en/latest/
.. _conda: http://docs.readthedocs.io/en/latest/conda.html

.. _installation:

Installation procedure
======================

Pip
---

You can use pip to install BioAPI of the latest stable version:

.. code-block:: bash

    pip install bioapi

Manually
--------

.. Note::
    This is particularly useful when you wish to install a version under development from
    any branches of the Github repository.

Clone the repository and install BioAPI with the following commands:

.. code-block:: bash

    git clone https://github.com/khillion/bioapi.git
    cd bioapi
    pip install .

.. _uninstallation:

Uninstallation procedure
=========================

Pip
---

You can remove BioAPI with the following command:

.. code-block:: bash

    pip uninstall bioapi

.. Note::
    This will not uninstall dependencies. To do so you can make use of the pip-autoremove
    tool `pip-autoremove`_ or set up your environment with pipenv_ or poetry_...

.. _pip-autoremove: https://github.com/invl/pip-autoremove
.. _pipenv: https://github.com/pypa/pipenv
.. _poetry: https://python-poetry.org/docs/
