# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html


from edgar_crawler.items import CompanyItem
from edgar_crawler.database import Database


class EdgarCrawlerPipeline(object):
    def __init__(self):
        self.db = Database()
        self.conn = self.db.getConn()
        self.cursor = self.conn.cursor()
    def process_item(self, item, spider):
        if isinstance(item, CompanyItem):
            sql = "insert ignore edgar_company set cik = %s, sic = %s, company = %s,loc = %s"
            self.cursor.execute(sql,(item['cik'],item['sic'],item['company'],item['loc']))
            self.conn.commit()
        return item
