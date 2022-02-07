from aiohttp import web
from aiopg.sa import Engine


class Application(web.Application):
    config: dict = {}
    db: Engine = None
