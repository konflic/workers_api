from aiohttp import web

from app.routes import setup_routes
from app.config import config
from app.database import pg_context, setup_db


def create_app():
    app = web.Application(debug=True)
    app["config"] = config
    setup_routes(app)
    setup_db(app["config"])
    app.cleanup_ctx.append(pg_context)
    return app


if __name__ == "__main__":
    web.run_app(create_app(), port=config["app"]["port"])
