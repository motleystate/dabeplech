from .version import __version__  # noqa

from .kegg import KEGGAPI  # noqa
from .ncbi_taxonomy import NCBITaxonomyScrapAPI  # noqa
from .togows import TogoWSEntryAPI  # noqa
from .metagenedb import (  # noqa
    MetageneDBTokenAPI,
    MetageneDBCatalogEggNOGAPI,
    MetageneDBCatalogGeneAPI,
    MetageneDBCatalogKeggOrthologyAPI,
    MetageneDBCatalogTaxonomyAPI,
    MetageneDBCatalogFunctionAPI
)
from .pdbe import (  # noqa
    PDBeAPI,
    PDBeUniprotMappingAPI,
    PDBePFAMMappingAPI,
)
from .doi import (  # noqa
    DOIAPI,
)
from .hal import (  #noqa
    HALAPI,
)
