#!/usr/bin/env/ python
# encoding: utf-8

"""
Cryptonator API wrapper library.
Meant to be as simple as possible.
"""

import requests

__author__ = 'aldur'
__version__ = '0.0.4'

API_CURRENCIES = "https://www.cryptonator.com/api/currencies"
API_SIMPLE_TICKER = "https://api.cryptonator.com/api/ticker/{}-{}"


class CryptonatorException(Exception):
    """Custom exception to be thrown on API error."""
    pass


def get_available_currencies():
    """Return a list of all available Cryptonator currencies."""
    r = requests.get(API_CURRENCIES)
    if r.status_code != requests.codes.ok:
        raise CryptonatorException(
            ("An error occurred while getting available currencies "
             "({} from Cryptonator).").format(r.status_code)
        )

    return [currency['code'] for currency in r.json()['rows']]


class Cryptonator(object):

    """
    Cryptonator API object.
    """

    def __init__(self):
        self.session = requests.Session()  # Use connection pooling for multiple requests.
        self.session.headers.update({'User-Agent': 'CryptonatorApi/{}'.format(__version__)})

    def get_exchange_rate(self, base, target, raise_errors=True):
        """Return the ::base:: to ::target:: exchange rate."""
        assert base and target

        base, target = base.lower(), target.lower()

        r = self.session.get(API_SIMPLE_TICKER.format(base, target))
        if r.status_code != requests.codes.ok:
            if not raise_errors:
                return None
            raise CryptonatorException(
                ("An error occurred while getting requested exchange rate "
                 "({} from Cryptonator).").format(r.status_code)
            )

        j = r.json()
        if not j['success'] or j['error']:
            if not raise_errors:
                return None
            raise CryptonatorException(
                ("An error occurred while getting requested exchange rate ({}, {})"
                 "('{}').").format(base, target, j['error'])
            )

        return float(j['ticker']['price'])

    def get_exchange_rates(self, base, targets=None, raise_errors=False):
        """Return the ::base:: to ::targets:: exchange rate (as a dictionary)."""
        if targets is None:
            targets = get_available_currencies()

        return {t: self.get_exchange_rate(base, t, raise_errors=raise_errors) for t in targets}


def get_exchange_rate(base, target, *args, **kwargs):
    """
    Return the ::base:: to ::target:: exchange rate.
    Wraps around ::Cryptonator.get_exchange_rate::.
    """
    return Cryptonator().get_exchange_rate(base, target, *args, **kwargs)
