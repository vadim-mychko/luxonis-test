import os

DATABASE_CONFIG = dict(
    database=os.environ.get("POSTGRES_DB"),
    user=os.environ.get("POSTGRES_USER"),
    password=os.environ.get("POSTGRES_DB"),
    host="localhost",
    port="5432"
)
