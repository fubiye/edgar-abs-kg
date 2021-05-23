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

class CompanyFilingItem(scrapy.Item):
    cik = scrapy.Field()
    filing = scrapy.Field()
    docs_link = scrapy.Field()
    filing_desc = scrapy.Field()
    effective = scrapy.Field()
    file_num = scrapy.Field()
    file_num_raw = scrapy.Field()
class CompanyFilingStateItem(scrapy.Item):
    cik = scrapy.Field()
    category = scrapy.Field()
    state = scrapy.Field()
class FileDownloadRecordItem(scrapy.Item):
    path = scrapy.Field()
    state = scrapy.Field()

class FileDownloadItem(scrapy.Item):
    file_urls = scrapy.Field()
    files = scrapy.Field()

class FilingFileItem(scrapy.Item):
    filing_id = scrapy.Field()
    seq = scrapy.Field()
    description = scrapy.Field()
    doc_name = scrapy.Field()
    doc_link = scrapy.Field()
    doc_type = scrapy.Field()
    size = scrapy.Field()