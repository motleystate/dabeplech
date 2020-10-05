"""
Script to test the status of different endpoints.

This script is aimed to be run locally to check the availability of different endpoints.
"""
import argparse
import logging
import sys

from kegg_api_status import test_keggapi
from togows_api_status import test_togowsentryapi
from pdbe_api_status import test_pdbeapi
from doi_api_status import test_doiapi
from hal_api_status import test_halapi

logging.basicConfig()
logger = logging.getLogger()


def parse_arguments():
    parser = argparse.ArgumentParser(description='Test the status of different endpoints supported by dabeplech.')
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
    test_keggapi()
    test_pdbeapi()
    test_doiapi()
    test_halapi()


if __name__ == "__main__":
    run()
