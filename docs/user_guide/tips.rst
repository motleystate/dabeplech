****
Tips
****

Use requests-cache
==================

The `requests-cache`_ library is installed with ``dabeplech``.

Using the Monkey-patching feature of the ``requests-cache`` library, caching will be used for all requests.

.. code-block:: python

    import requests_cache

    requests_cache.install_cache(backend="memory")

.. Note::
     By default, it uses a ``sqlite`` db but you can also use ``memory``, ``redis`` or ``mongodb`` instead.

.. _requests-cache: https://requests-cache.readthedocs.io/en/latest/user_guide.html