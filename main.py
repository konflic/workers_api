from aiohttp import web

from app.routes import setup_routes
from settings.config import config
from app.db import pg_context

app = web.Application()
app["config"] = config

setup_routes(app)
app.cleanup_ctx.append(pg_context)
web.run_app(app)
