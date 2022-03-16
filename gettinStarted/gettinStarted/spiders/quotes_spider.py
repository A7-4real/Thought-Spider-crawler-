from curses import pair_number
from unicodedata import name
import scrapy


class QuotesSpider(scrapy.spider):
    name = 'quotes'

    def start_request(self):
        urls = [
            "https://quotes.toscrape.com/page/1",
            "https://quotes.toscrape.com/page/2",

        ]

        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        page = response.url.split("/")[-2]
        filename = f'quotes-{page}.html'
        with open(filename, 'wb') as f:
            f.write(response.body)
        self.log(f'saved file {filename}')
