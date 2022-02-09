from aiohttp import web

from app.routes import setup_routes
from src.config import config
from app.database import pg_context, setup_db
from src.application import Application


def create_app(debug=False):
    app = Application(debug=debug)
    setup_routes(app)
    setup_db(app.config)
    app.cleanup_ctx.append(pg_context)
    return app


if __name__ == "__main__":
    web.run_app(create_app(), port=config["app"]["port"])
