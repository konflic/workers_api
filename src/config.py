import os
from dotenv import load_dotenv

load_dotenv()

config = {
    "postgres": {
        "database": os.getenv("DB_DATABASE", "workers"),
        "user": os.getenv("DB_USER", "postgres"),
        "password": os.getenv("DB_PASSWORD", "password"),
        "host": os.getenv("DB_HOST", "localhost"),
        "port": os.getenv("DB_PORT", 5432),
    },
    "app": {
        "host": os.getenv("APP_HOST", "localhost"),
        "port": os.getenv("APP_PORT", 8080),
    },
}
