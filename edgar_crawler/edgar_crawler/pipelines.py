# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html


import os
from scrapy.http.request import Request
from scrapy.pipelines.files import FilesPipeline
from urllib.parse import urlparse

from edgar_crawler.items import CompanyItem, CompanyFilingItem,CompanyFilingStateItem,FileDownloadRecordItem, FilingFileItem
from edgar_crawler.database import Database
from edgar_crawler.constants import SEC_HOSTNAME


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
        if isinstance(item, FileDownloadRecordItem):
            sql = "insert into edgar_file_log set file_path = %s, state = %s"
            self.cursor.execute(sql,(item['path'],item['state']))
            self.conn.commit()
        if isinstance(item, FilingFileItem):
            sql = "insert ignore edgar_filing_file set filing_id = %s, seq = %s, description = %s, doc_name = %s, doc_link = %s, doc_type = %s, size = %s"
            self.cursor.execute(sql,(item['filing_id'],item['seq'],item['description'],item['doc_name'],item['doc_link'],item['doc_type'],item['size']))
            self.conn.commit()
        return item

class MyFilesPipeline(FilesPipeline):
    def __init__(self, store_uri, download_func=None, settings=None):
        super().__init__(store_uri, download_func=download_func, settings=settings)
        self.db = Database()
        self.conn = self.db.getConn()
        self.cursor = self.conn.cursor()
    def file_path(self, request, response=None, info=None):
        return urlparse(request.url).path
        
    def item_completed(self, results, item, info):
        item = super().item_completed(results, item, info)
        if 'files' in item and len(item['files']) > 0:
            for file in item['files']:
                sql = "insert into edgar_file_log set file_path = %s, state = %s"
                self.cursor.execute(sql,(file['path'],'done'))
                self.conn.commit()
        return item