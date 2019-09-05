import logging

from bioapi import (
    TogoWSEntryAPI,
)

"""
Script to test the status of different endpoints.

This script is aimed to be run locally to check the availability of different endpoints.
"""


def _red_text(text):
    return f'\033[31m{text}\033[m'


def _green_text(text):
    return f'\033[32m{text}\033[m'


def test_togowsentryapi():
    print("---------- Testing TogoWS API endpoints... ----------")
    tests = {
        'kegg-pathway': 'ko05132',
        'kegg-orthology': 'K00001',
    }
    for db, entry_id in tests.items():
        print(f"Test getting {entry_id} from {db} database from {TogoWSEntryAPI.BASE_URL}... ", end='')
        try:
            api = TogoWSEntryAPI(db)
            api.get(entry_id)
            print(_green_text('OK'))
        except:
            print(_red_text("ERROR"))


def run():
    test_togowsentryapi()


if __name__ == "__main__":
    run()