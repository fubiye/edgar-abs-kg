# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html


from edgar_crawler.items import CompanyItem, CompanyFilingItem,CompanyFilingStateItem
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
        if isinstance(item, CompanyFilingItem):
            sql = "insert ignore edgar_company_filing set cik = %s, filing = %s, docs_link = %s,filing_desc = %s,effective = %s, file_num = %s, file_num_raw = %s"
            self.cursor.execute(sql,(item['cik'],item['filing'],item['docs_link'],item['filing_desc'],item['effective'],item['file_num'],item['file_num_raw']))
            self.conn.commit()
        if isinstance(item, CompanyFilingStateItem):
            sql = "insert into edgar_company_filing_craw_log set cik = %s, category = %s, state = %s"
            self.cursor.execute(sql,(item['cik'],item['category'],item['state']))
            self.conn.commit()
        return item
