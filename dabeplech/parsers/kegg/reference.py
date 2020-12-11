"""Parsers for references items in KEGG responses."""
import logging

from dabeplech.models.kegg import KeggReferenceModel

logging.basicConfig()
logger = logging.getLogger()


class KeggReferenceParser:
    """
    Simple class that handle parsing of the REFERENCE part from KEGG API.

    It is build with the idea of setter handling each line directly

    e.g.:
    ```
    parser.pubmed_id = 'REFERENCE    PMID:124142"
    print(parser.pubmed_id)
    124142
    ```
    """

    model = KeggReferenceModel

    @property
    def pubmed_id(self):
        """Get pubmed ID for this reference."""
        return self._pubmed_id

    @pubmed_id.setter
    def pubmed_id(self, line: str):
        if "PMID" not in line:
            logger.warning("no PMID for the reference. Corresponding line: %s", line)
            self._pubmed_id = None
        else:
            self._pubmed_id = line.split()[1].split("PMID:")[-1].strip()

    @property
    def authors(self):
        """Get authors for this reference."""
        return self._authors

    @authors.setter
    def authors(self, line):
        all_authors = line.split(maxsplit=1)[-1].split(",")
        self._authors = [author.strip() for author in all_authors]

    @property
    def title(self):
        """Get title for this reference."""
        return self._title

    @title.setter
    def title(self, line):
        self._title = line.split(maxsplit=1)[-1]

    @property
    def journal(self):
        """Get journal for this reference."""
        return self._journal

    @journal.setter
    def journal(self, line):
        self._journal = line.split(maxsplit=1)[-1]

    @property
    def doi(self):
        """Get DOI for this reference."""
        return self._doi

    @doi.setter
    def doi(self, line):
        self._doi = line.split("DOI:", maxsplit=1)[-1]

    def dict(self) -> dict:
        """Get reference as a dict."""
        return self.model(
            **{
                "pubmed_id": getattr(self, "pubmed_id", None),
                "authors": getattr(self, "authors", None),
                "title": getattr(self, "title", None),
                "journal": getattr(self, "journal", None),
                "doi": getattr(self, "doi", None),
            }
        ).dict()
