import random
import time

import aiohttp
import requests

from requests import HTTPError
from xml.etree import ElementTree

from twirp.asgi import TwirpASGIApp
from twirp.exceptions import InvalidArgument

import currency_twirp, currency_pb2


class GetCurrencyService(object):
    async def GetDollarRate(self, context, _):
        url = 'http://www.cbr.ru/scripts/XML_daily.asp'

        start = time.time()
        async with aiohttp.ClientSession() as session:
            async with session.get(url) as resp:
               data = await resp.text()

        end = time.time()

        print(end - start)

        tree = ElementTree.fromstring(data)

        usd_node = None
        for node in tree.getchildren():
            if node.attrib['ID'] == 'R01235':
                usd_node = node
                break

        value = None
        for attr in usd_node.getchildren():
            if attr.tag == 'Value':
                value = attr.text

        return currency_pb2.Rates(
            # rates=data,
            rates=value,
        )


service = currency_twirp.CurrencyRatesServer(service=GetCurrencyService())
app = TwirpASGIApp()
app.add_service(service)



