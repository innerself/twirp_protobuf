import random

from twirp.asgi import TwirpASGIApp
from twirp.exceptions import InvalidArgument

import service_twirp, service_pb2


class HaberdasherService(object):
    async def MakeHat(self, context, size):
        if size.inches <= 0:
            raise InvalidArgument(argument="inches", error="I can't make a hat that small!")
        return service_pb2.Hat(
            size=size.inches,
            color=random.choice(["white", "black", "brown", "red", "blue"]),
            name=random.choice(["bowler", "baseball cap", "top hat", "derby"])
        )


# if you are using a custom prefix, then pass it as `server_path_prefix`
# param to `HaberdasherServer` class.
service = service_twirp.HaberdasherServer(service=HaberdasherService())
app = TwirpASGIApp()
app.add_service(service)
