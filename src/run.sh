# apparently it is really hard to wait for the database to
# be properly set up before executing scripts...
# the wait-for-it.sh is from https://github.com/vishnubob/wait-for-it

export POSTGRES_USER="scrapy"
export POSTGRES_HOST="db"
export POSTGRES_DB="scrapy"
export POSTGRES_PASSWORD="admin"

until /app/src/wait-for-it.sh -h $POSTGRES_HOST -p 5432 -t 5; do
    echo "Waiting for PostgreSQL..."
done

scrapy runspider /app/src/flat_spider.py
python /app/src/update_database.py /app/scraped_data.json
python /app/src/server.py
