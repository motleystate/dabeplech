**********************
Contributing to BioAPI
**********************

You have many different ways to contribute to BioAPI:

- Add new API connectors
- Report a Bug
- Suggesting a new Feature
- Update the Documentation
- Participate to the discussions in the Github issues

.. Note::
    For more advanced features, such as the code architecture, we encourage to go through discussions on GitHub
    before starting any major changes or contributions.

General rules
=============

- :ref:`contrib_environment`: set up your environment to contribute.
- :ref:`contrib_flow`: contribution through GitHub.
- :ref:`contrib_conduct`

Adding a new API connector
==========================

For the moment, we identify two different scenarios when adding a new API connector,
either the API already return some JSON format or the API return another format and needs
some parsing and formatting to stick to the openapi standard.

API already returning JSON
--------------------------

This is the most simple case where you just need to add a new connector:

1. :ref:`contrib_api`
2. :ref:`contrib_docs`

API returning different format
------------------------------

1. :ref:`contrib_model`
2. :ref:`contrib_parser`
3. :ref:`contrib_api_parser`
4. :ref:`contrib_docs`
