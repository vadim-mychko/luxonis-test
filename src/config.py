import os

DATABASE_CONFIG = dict(
    database="scrapy",
    user="mychkvad",
    password=os.environ.get("SCRAPY_PASSWORD"),
    host="localhost",
    port="5432"
)
