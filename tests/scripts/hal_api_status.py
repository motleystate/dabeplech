from dabeplech import HALAPI

from utils import _format_print


def _expected_working_hal():
    tests = [
        ('10.12688/f1000research.12974.1', HALAPI)
    ]
    for i in tests:
        entry_id = i[0]
        api_connector = i[1]
        api = api_connector()
        print(f"Test getting {entry_id} from HAL database from base URL: {api.BASE_URL}:")
        try:
            content = api.find(doi=entry_id)  # noqa
            print(_format_print("Status", "OK", "green"))
            if content:
                print(_format_print(f"Content (format:{type(content)})", "NOT EMPTY", "green"))
            else:
                print(_format_print("Content", "EMPTY", "red"))
        except Exception:
            print(_format_print("Status", "ERROR", "red"))
        finally:
            print(f" --> Requested URL: {api.last_url_requested}")


def _expected_not_working_hal():
    tests = [
        ('10.12688f1000research.12974.1', HALAPI)
    ]
    for i in tests:
        entry_id = i[0]
        api_connector = i[1]
        api = api_connector()
        print(f"Test getting {entry_id} from HAL database from base URL: {api.BASE_URL}:")
        try:
            api = api_connector()
            content = api.get(doi=entry_id)  # noqa
            print(_format_print("Status", "OK", "red"))
        except Exception:
            print(_format_print("Status", "ERROR", "green"))
        finally:
            print(f" --> Requested URL: {api.last_url_requested}")


def test_halapi():
    print("---------- Testing DOI API endpoints... ----------")
    _expected_working_hal()
    _expected_not_working_hal()
