from urllib.parse import urljoin

from requests.exceptions import HTTPError

from .base import BaseAPI


class TogoWSAPI(BaseAPI):
    BASE_URL = 'http://togows.org'


class TogoWSEntryAPI(TogoWSAPI):
    TYPE = 'entry'
    DATABASES = [
        'ncbi-nuccore',
        'ncbi-nucest',
        'ncbi-nucgss',
        'ncbi-nucleotide',
        'ncbi-protein',
        'ncbi-gene',
        'ncbi-homologene',
        'ncbi-snp',
        'ncbi-mesh',
        'ncbi-pubmed',
        'ebi-ena',
        'ebi-uniprot',
        'ebi-uniparc',
        'ebi-uniref100',
        'ebi-uniref90',
        'ebi-uniref50',
        'ddbj-ddbj',
        'ddbj-dad',
        'pdbj-pdb',
        'kegg-compound',
        'kegg-drug',
        'kegg-enzyme',
        'kegg-genes',
        'kegg-glycan',
        'kegg-orthology',
        'kegg-reaction',
        'kegg-module',
        'kegg-pathway'
    ]

    def __init__(self, database, entry_format='json'):
        super().__init__()
        if database not in self.DATABASES:
            raise ValueError(f"{database} is not a valid database")
        self.database = database
        self.format = entry_format
        self.route = f"{self.TYPE}/{self.database}/"
        self.url = urljoin(self.BASE_URL, self.route)

    def get(self, entry_id):
        content = super().get(f"{entry_id}.{self.format}")
        if not content:
            raise HTTPError("%s not found in %s", entry_id, self.url)
        return content

    def get_field(self, entry_id, field):
        return super().get(f"{entry_id}/{field}.{self.format}")
