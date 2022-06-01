import requests
import json
from config import keys

class ConvertionException(Exception):
    pass

class CryptoConverter:
    @staticmethod
    def get_price(quote: str, base: str, amount: float):

        if quote == base:
            raise ConvertionException(f'А зачем одинаковые валюты конвертировать? {base} и {base}.')

        try:
            quote_ticker = keys[quote]

        except KeyError:
            raise ConvertionException(f'Я не знаю такую валюту - {quote}.')

        try:
            base_ticker = keys[base]

        except KeyError:
            raise ConvertionException(f'Я не знаю такую валюту - {base}.')

        try:
            amount = float(amount)

        except ValueError:
            raise ConvertionException(f'А {amount} - это сколько в цифрах? ')

        r = requests.get(f'https://min-api.cryptocompare.com/data/price?fsym={quote_ticker}&tsyms={base_ticker}')
        total_base = json.loads(r.content)[keys[base]]

        return total_base