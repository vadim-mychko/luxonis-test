import json
from scrapy import Spider, Request


class FlatSpider(Spider):
    name = "flats"

    def start_requests(self):
        url = (
            "https://www.sreality.cz/api/en/v2/estates"
            "?category_main_cb=1&category_type_cb=1&page=1&per_page=500"
        )
        yield Request.from_curl(f"curl '{url}'")

    def parse(self, response):
        data = json.loads(response.text)
        flats = data["_embedded"]["estates"]
        scraped_data = {"data": []}

        for flat in flats:
            name = flat["name"]
            url = flat["_links"]["images"][0]["href"]
            scraped_data["data"].append({"name": name, "url": url})

        filename = "scraped_data.json"
        with open(filename, "w", encoding="utf-8") as file:
            json.dump(scraped_data, file, indent=4)

        self.log(f"Saved scraped data to the {filename}")
