# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class EdgarCrawlerItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    pass
class CompanyItem(scrapy.Item):
    sic = scrapy.Field()
    cik = scrapy.Field()
    company = scrapy.Field()
    loc = scrapy.Field()