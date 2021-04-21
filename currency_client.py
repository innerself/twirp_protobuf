from twirp.context import Context
from twirp.exceptions import TwirpServerException

import currency_twirp, currency_pb2

client = currency_twirp.CurrencyRatesClient("http://127.0.0.1:3000")

# if you are using a custom prefix, then pass it as `server_path_prefix`
# param to `MakeHat` class.
try:
    response = client.GetDollarRate(ctx=Context(), request=currency_pb2.Nothing())
    print(response)
except TwirpServerException as e:
    print(e.code, e.message, e.meta, e.to_dict())
