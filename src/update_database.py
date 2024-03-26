import os
import json
import psycopg2
from argparse import ArgumentParser
from pathlib import Path
from psycopg2.extras import execute_values


def main():
    parser = ArgumentParser(description="Adds scraped data to the database")
    parser.add_argument("datapath", help="path to the .json file")
    args = parser.parse_args()
    datapath = Path(args.datapath)

    conn = psycopg2.connect(
        database="scrapy",
        user="mychkvad",
        password=os.environ.get("SCRAPY_PASSWORD"),
        host="localhost",
        port="5432"
    )

    cur = conn.cursor()
    cur.execute(
        """CREATE TABLE IF NOT EXISTS data (
            id SERIAL PRIMARY KEY,
            name VARCHAR(255) NOT NULL,
            url TEXT NOT NULL
        )"""
    )

    with open(datapath, "r") as file:
        data = json.load(file)

    data = [(item["name"], item["url"]) for item in data["data"]]
    query = "INSERT INTO Data (name, url) VALUES %s"
    execute_values(cur, query, data)
    conn.commit()

    cur.close()
    conn.close()


if __name__ == "__main__":
    main()
