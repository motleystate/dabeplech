import logging

logging.basicConfig()
logger = logging.getLogger()


class KeggReferenceParser:
    """
    Simple class that handle parsing of the REFERENCE part from KEGG API

    It is build with the idea of setter handling each line directly

    e.g.:
    ```
    parser.pubmed_id = 'REFERENCE    PMID:124142"
    print(parser.pubmed_id)
    124142
    ```
    """

    @property
    def pubmed_id(self):
        return self._pubmed_id

    @pubmed_id.setter
    def pubmed_id(self, line: str):
        """
        :param line: corresponding line
        :type line: STR
        """
        if 'PMID' not in line:
            logger.warning("no PMID for the reference. Corresponding line: %s", line)
            self._pubmed_id = None
        else:
            self._pubmed_id = line.split()[1].split('PMID:')[-1].strip()

    @property
    def authors(self):
        return self._authors

    @authors.setter
    def authors(self, line):
        all_authors = line.split(maxsplit=1)[-1].split(',')
        self._authors = [author.strip() for author in all_authors]

    @property
    def title(self):
        return self._title

    @title.setter
    def title(self, line):
        self._title = line.split(maxsplit=1)[-1]

    @property
    def journal(self):
        return self._journal

    @journal.setter
    def journal(self, line):
        self._journal = line.split(maxsplit=1)[-1]

    @property
    def doi(self):
        return self._doi

    @doi.setter
    def doi(self, line):
        self._doi = line.split('DOI:', maxsplit=1)[-1]

    def dict(self):
        return {
            'pubmed_id': getattr(self, 'pubmed_id', None),
            'authors': getattr(self, 'authors', None),
            'title': getattr(self, 'title', None),
            'journal': getattr(self, 'journal', None),
            'doi': getattr(self, 'doi', None),
        }
