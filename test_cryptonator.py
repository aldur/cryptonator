#!/usr/bin/env/ python
# encoding: utf-8

import collections
import unittest
import numbers

import cryptonator

__author__ = 'aldur'


class CryptonatorTestCase(unittest.TestCase):
    def test_get_available_currencies(self):
        self.assertIsNotNone(cryptonator.get_available_currencies())

    def test_get_eur_usd_exchange_rate(self):
        self.assertIsInstance(cryptonator.get_exchange_rate('eur', 'usd'), numbers.Real)

    def get_get_eur_exchange_rates(self):
        self.assertIsInstance(cryptonator.Cryptonator().get_exchange_rates('eur', ['usd', 'btc']), collections.Sequence)

    def test_get_bad_exchange_rate_no_raise_errors(self):
        self.assertIsNone(cryptonator.get_exchange_rate('foo', 'bar', raise_errors=False))

    def test_get_bad_exchange_rate_raise_errors(self):
        with self.assertRaises(cryptonator.CryptonatorException):
            cryptonator.get_exchange_rate('foo', 'bar')

if __name__ == '__main__':
    unittest.main()
