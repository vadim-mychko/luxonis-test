from pathlib import Path

from scrapy import Spider


class FlatSpider(Spider):
    name = "flats"

    start_urls = [
        "https://sreality.cz/en/search/for-sale/apartments"
    ]

    def parse(self, response):
        filename = "temp.html"
        Path(filename).write_bytes(response.body)
        self.log(f"Saved file {filename}")
