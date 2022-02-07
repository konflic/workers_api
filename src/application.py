from aiohttp import web
from aiopg.sa import Engine
from app.config import config


class Application(web.Application):
    config: dict = config
    db: Engine = None
