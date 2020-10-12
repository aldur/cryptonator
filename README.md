# Cryptonator Python API

A simple wrapper for the [Cryptonator](https://www.cryptonator.com/api/) exchange rate API.

## Install

You can either install Cryptonator by using `pip`, or simply copy the
`cryptonator.py` file in you project root directory.

```bash
$ pip install cryptonator  # add --user if you want
```

## Usage

```python
import cryptonator

"""Get an exchange rate between two currencies."""
cryptonator.get_exchange_rate('usd', 'eur')
# 0.95147479

"""A Cryptonator API object can speed-up things if you need multiple calls."""
api = cryptonator.Cryptonator()

"""Get an exchange rate between a single curreny and many targets."""
api.get_exchange_rates('usd', ['eur', 'btc', 'xrp'])
# {'btc': 0.00136076, 'eur': 0.95147479, 'xrp': 144.71780029}
```

## Testing

Tests can be found in `test_cryptonator.py`.
You can launch them with:

```bash
$ python test_cryptonator.py
```
