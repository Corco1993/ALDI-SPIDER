import scrapy
from ..items import FinalItem
from scrapy.loader import ItemLoader


class aldi2(scrapy.Spider):
    name = 'final'
    start_urls = ['https://www.aldi.nl/producten.html']

    def parse(self, response):
        for link in response.css('.mod-content-tile__action::attr(href)'):
            yield response.follow('https://www.aldi.nl' + link.get(), callback=self.parse_subcateg)

    def parse_subcateg(self, response):

        for link in response.css('.mod-content-tile__action::attr(href)'):
            yield response.follow('https://www.aldi.nl' + link.get(), callback=self.parse_product)

    def parse_product(self,response):
        products = response.css('div.tiles.parbase')
        for p in products:
            il = ItemLoader(item=FinalItem(), selector=p)

            il.add_css('title', 'span.mod-article-tile__title')
            il.add_css('price', 'span.price__wrapper')
            il.add_css('unit', 'span.price__unit')

            yield il.load_item()