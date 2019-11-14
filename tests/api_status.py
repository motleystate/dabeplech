"""
Script to test the status of different endpoints.

This script is aimed to be run locally to check the availability of different endpoints.
"""
import argparse
import logging

import colored

from bioapi import (
    TogoWSEntryAPI,
)


logging.basicConfig()
logger = logging.getLogger()


def _format_print(key_word, msg, color=None):
    """
    Format message such as:
      --> {key_word} ... {msg}
    """
    if color:
        return f" --> {key_word} ... {colored.stylize(msg, colored.fg(color))}"
    return f" --> {key_word} ... {msg}"


def expected_working_togowsentry():
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
            content = api.get(entry_id)
            print(_format_print("Status", "OK", "green"))
            if content:
                print(_format_print("Content", "NOT EMPTY", "green"))
            else:
                print(_format_print("Content", "EMPTY", "red"))
        except:
            print(_format_print("Status", "ERROR", "red"))


def expected_not_working_togowsentry():
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
            content = api.get(entry_id)
            print(_format_print("Status", "OK", "red"))
        except:
            print(_format_print("Status", "ERROR", "green"))


def test_togowsentryapi():
    print("---------- Testing TogoWS API endpoints... ----------")
    expected_working_togowsentry()
    expected_not_working_togowsentry()


def parse_arguments():
    parser = argparse.ArgumentParser(description='Test the status of different endpoints supported by bioapi.')
    parser.add_argument('--verbose', action='store_true')
    parser.add_argument('--debug', action='store_true')

    try:
        return parser.parse_args()
    except SystemExit:
        sys.exit(1)


def run():
    args = parse_arguments()
    if args.verbose:
        logger.setLevel(logging.INFO)
    if args.debug:
        logger.setLevel(logging.DEBUG)
    test_togowsentryapi()


if __name__ == "__main__":
    run()