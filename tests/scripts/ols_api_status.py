from dabeplech import OLSAPI

from utils import _format_print


def _expected_working_ols():
    tests = [
        ('GO_0008150', OLSAPI)
    ]
    for i in tests:
        entry_id = i[0]
        api_connector = i[1]
        api = api_connector()
        print(f"Test getting {entry_id} from GO database from OLS base URL: {api.BASE_URL}:")
        try:
            content = api.get_term(entry_id)  # noqa
            print(_format_print("Status", "OK", "green"))
            if content:
                print(_format_print(f"Content (format:{type(content)})", "NOT EMPTY", "green"))
            else:
                print(_format_print("Content", "EMPTY", "red"))
        except Exception:
            print(_format_print("Status", "ERROR", "red"))
        finally:
            print(f" --> Requested URL: {api.last_url_requested}")


def _expected_not_working_ols():
    tests = [
        ('GA_0008150', OLSAPI)
    ]
    for i in tests:
        entry_id = i[0]
        api_connector = i[1]
        api = api_connector()
        print(f"Test getting {entry_id} from GO database from OLS base URL: {api.BASE_URL}:")
        try:
            api = api_connector()
            content = api.get_term(entry_id)  # noqa
            print(_format_print("Status", "OK", "red"))
        except Exception:
            print(_format_print("Status", "ERROR", "green"))
        finally:
            print(f" --> Requested URL: {api.last_url_requested}")


def test_olsapi():
    print("---------- Testing DOI API endpoints... ----------")
    _expected_working_ols()
    _expected_not_working_ols()
