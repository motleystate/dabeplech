from dabeplech import PDBeUniprotMappingAPI, PDBePFAMMappingAPI

from utils import _format_print


def _expected_working_pdbe():
    tests = [
        ('Uniprot Mappings', '3u85', PDBeUniprotMappingAPI),
        ('PFAM Mappings', '3u85', PDBePFAMMappingAPI),
    ]
    for i in tests:
        db = i[0]
        entry_id = i[1]
        api_connector = i[2]
        api = api_connector()
        print(f"Test getting {entry_id} from {db} database from base URL: {api.BASE_URL}:")
        try:
            content = api.get(entry_id)  # noqa
            print(_format_print("Status", "OK", "green"))
            if content:
                print(_format_print(f"Content (format:{type(content)})", "NOT EMPTY", "green"))
            else:
                print(_format_print("Content", "EMPTY", "red"))
        except Exception:
            print(_format_print("Status", "ERROR", "red"))
        finally:
            print(f" --> Requested URL: {api.last_url_requested}")


def _expected_not_working_pdbe():
    tests = [
        ('Uniprot Mappings', 'Xu85', PDBeUniprotMappingAPI),
        ('PFAM Mappings', 'Xu85', PDBePFAMMappingAPI),
    ]
    for i in tests:
        db = i[0]
        entry_id = i[1]
        api_connector = i[2]
        api = api_connector()
        print(f"Test getting {entry_id} from {db} database from base URL: {api.BASE_URL}:")
        try:
            api = api_connector()
            content = api.get(entry_id)  # noqa
            print(_format_print("Status", "OK", "red"))
        except Exception:
            print(_format_print("Status", "ERROR", "green"))
        finally:
            print(f" --> Requested URL: {api.last_url_requested}")


def test_pdbeapi():
    print("---------- Testing PDBe API endpoints... ----------")
    _expected_working_pdbe()
    _expected_not_working_pdbe()
