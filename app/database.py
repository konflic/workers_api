import aiopg.sa

from sqlalchemy import MetaData, Table, Column, Integer, String

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


async def pg_context(app):
    conf = app["config"]["postgres"]

    engine = await aiopg.sa.create_engine(
        database=conf["database"],
        user=conf["user"],
        password=conf["password"],
        host=conf["host"],
        port=conf["port"],
    )

    app["db"] = engine

    yield

    app["db"].close()
    await app["db"].wait_closed()
