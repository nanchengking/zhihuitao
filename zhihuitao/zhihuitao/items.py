# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html
import scrapy
from scrapy.item import Field
class ZhihuitaoItem(scrapy.Item):
    title = Field()
    content = Field()
    url = Field()
