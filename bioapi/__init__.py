from .version import __version__

from .kegg import KEGGAPI  # noqa
from .togows import TogoWSEntryAPI  # noqa
from .metagenedb import (  # noqa
    MetageneDBCatalogEggNOGAPI,
    MetageneDBCatalogGeneAPI,
    MetageneDBCatalogKeggOrthologyAPI,
    MetageneDBCatalogTaxonomyAPI,
    MetageneDBCatalogFunctionAPI
)
