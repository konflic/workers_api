from aiohttp import web

from app.routes import setup_routes
from app.config import config
from app.database import pg_context
from init_db import setup_db

app = web.Application()
app["config"] = config

setup_routes(app)
setup_db(app["config"])
app.cleanup_ctx.append(pg_context)
web.run_app(app, port=8888)
