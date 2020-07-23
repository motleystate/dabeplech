from dabeplech import TogoWSEntryAPI

from utils import _format_print


def _expected_not_working_togowsentry():
    tests = [
        ('kegg-pathway', 'ko05132222'),
        ('kegg-orthology', 'K000011111'),
        ('kegg-orthology', 'no_way')
    ]
    for i in tests:
        db = i[0]
        entry_id = i[1]
        print(f"Test getting {entry_id} from {db} database from {TogoWSEntryAPI.BASE_URL}:")
        try:
            api = TogoWSEntryAPI(db)
            content = api.get(entry_id)  # noqa
            print(_format_print("Status", "OK", "red"))
        except Exception:
            print(_format_print("Status", "ERROR", "green"))
        finally:
            print(f" --> Requested URL: {api.last_url_requested}")


def _expected_working_togowsentry():
    tests = [
        ('kegg-pathway', 'ko05132'),
        ('kegg-orthology', 'K00001'),
    ]
    for i in tests:
        db = i[0]
        entry_id = i[1]
        print(f"Test getting {entry_id} from {db} database from {TogoWSEntryAPI.BASE_URL}:")
        try:
            api = TogoWSEntryAPI(db)
            content = api.get(entry_id)  # noqa
            print(_format_print("Status", "OK", "green"))
            if content:
                print(_format_print("Content", "NOT EMPTY", "green"))
            else:
                print(_format_print("Content", "EMPTY", "red"))
        except Exception:
            print(_format_print("Status", "ERROR", "red"))
        finally:
            print(f" --> Requested URL: {api.last_url_requested}")


def test_togowsentryapi():
    print("---------- Testing TogoWS API endpoints... ----------")
    _expected_working_togowsentry()
    _expected_not_working_togowsentry()
