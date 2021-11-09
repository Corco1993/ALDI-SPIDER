# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy
from itemloaders.processors import MapCompose, TakeFirst
from w3lib.html import remove_tags



class FinalItem(scrapy.Item):
    # define the fields for your item here like:
    title = scrapy.Field(input_processor=MapCompose(remove_tags),output_processor=TakeFirst())
    price = scrapy.Field(input_processor=MapCompose(remove_tags),output_processor=TakeFirst())
    unit = scrapy.Field(output_processor=TakeFirst())

