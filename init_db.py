from sqlalchemy import MetaData, create_engine
from sqlalchemy_utils import create_database, database_exists

from app.database import workers


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
