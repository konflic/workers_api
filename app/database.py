import aiopg.sa

from sqlalchemy import Table, Column, Integer, String
from sqlalchemy import MetaData, create_engine
from sqlalchemy_utils import create_database, database_exists
from src.application import Application

meta = MetaData()

workers = Table(
    "workers",
    meta,
    Column("id", Integer, primary_key=True),
    Column("name", String(200), nullable=False),
    Column("department", String(200), nullable=False),
    Column("position", String(50), nullable=False),
    Column("grade", Integer, nullable=False),
    Column("birthday", String, nullable=False),
    Column("gender", String, nullable=False),
)


def setup_db(config):
    DSN = "postgresql://{user}:{password}@{host}:{port}/{database}"

    def create_tables(engine):
        meta = MetaData()
        meta.create_all(engine, tables=[workers])

    db_url = DSN.format(**config["postgres"])

    if not database_exists(db_url):
        create_database(db_url)
        engine = create_engine(db_url)
        create_tables(engine)

    print("DB and Tables setup and created!")


async def pg_context(app: Application):
    conf = app.config["postgres"]

    engine = await aiopg.sa.create_engine(
        database=conf["database"],
        user=conf["user"],
        password=conf["password"],
        host=conf["host"],
        port=conf["port"],
    )

    app.db = engine

    yield

    app.db.close()
    await app.db.wait_closed()
