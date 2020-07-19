.. BioAPI

.. _changelog:

**********
Changelogs
**********

Summary of developments of BioAPI library.

v0.0
====

v0.0.4
------

* Replace models for pathway and ko list by simpler model

v0.0.3
------

* Add parser and api for KEGG pathway list (https://github.com/khillion/bioapi/pull/10)
* Add parser and api for KEGG ko list (https://github.com/khillion/bioapi/pull/10)
* Change ``name`` attribute to ``names`` for KEGG
* Handle reference with no pubmed ID (https://github.com/khillion/bioapi/pull/7)

v0.0.2
------

* Add parser for KEGG pathway response

v0.0.1
------

This is the first release of BioAPI:

* Parser for KEGG orthology response
* Base structure for KEGG API

    * Return structured dict if parser available
    * If no parser available, return raw response from KEGG API

* Base structure for TogoWS API
