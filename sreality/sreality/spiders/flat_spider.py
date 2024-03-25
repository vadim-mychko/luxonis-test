import json

from pathlib import Path
from scrapy import Spider, Request


class FlatSpider(Spider):
    name = "flats"

    def start_requests(self):
        url = "https://www.sreality.cz/api/en/v2/estates?page=1&per_page=500"
        yield Request.from_curl(f"curl '{url}'")

    def parse(self, response):
        data = json.loads(response.text)
