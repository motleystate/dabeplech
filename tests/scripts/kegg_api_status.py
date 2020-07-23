from dabeplech import KEGGAPI

from utils import _format_print


def _expected_working_kegg():
    tests = [
        ('pathway', 'ko05132'),
        ('ko', 'K00001'),
    ]
    for i in tests:
        db = i[0]
        entry_id = i[1]
        print(f"Test getting {entry_id} from {db} database from base URL: {KEGGAPI.BASE_URL}:")
        try:
            api = KEGGAPI()
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


def _expected_not_working_kegg():
    tests = [
        ('pathway', 'ko05132222'),
        ('ko', 'K000011111'),
        ('ko', 'no_way')
    ]
    for i in tests:
        db = i[0]
        entry_id = i[1]
        print(f"Test getting {entry_id} from {db} database from base URL: {KEGGAPI.BASE_URL}:")
        try:
            api = KEGGAPI()
            content = api.get(entry_id)  # noqa
            print(_format_print("Status", "OK", "red"))
        except Exception:
            print(_format_print("Status", "ERROR", "green"))
        finally:
            print(f" --> Requested URL: {api.last_url_requested}")


def test_keggapi():
    print("---------- Testing KEGG API endpoints... ----------")
    _expected_working_kegg()
    _expected_not_working_kegg()
