from urllib.parse import urljoin

from requests.exceptions import HTTPError

from .base import BaseAPI, GETMixin


class TogoWSAPI(BaseAPI, GETMixin):
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
    FORMATS = [
        "json", "fasta", "gff", "ttl", "xml"
    ]

    def __init__(self, database: str, entry_format: str = 'json'):
        """
        :param database: selected target database (list in self.DATABASES)
        :param entry_format: format for the response
        """
        super().__init__()
        if database not in self.DATABASES:
            raise ValueError(f"{database} is not a valid database")
        if entry_format not in self.FORMATS:
            raise ValueError(f"{entry_format} is not a valid entry format")
        self.database = database
        self.format = entry_format
        self.route = f"{self.TYPE}/{self.database}/"
        self.url = urljoin(self.BASE_URL, self.route)

    def get(self, entry_id: str):
        """
        :param entry_id: ID to obtain from selected database
        """
        content = super().get(f"{entry_id}.{self.format}")
        if not content:
            raise HTTPError(f"ID: <{entry_id}> not found in {self.url}")
        return content[0]

    def get_field(self, entry_id: str, field: str):
        """
        :param entry_id: ID to obtain from selected database
        :param field: specific field to select in the response
        """
        return super().get(f"{entry_id}/{field}.{self.format}")
