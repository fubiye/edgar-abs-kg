from time import sleep
import scrapy
from edgar_crawler.database import Database
from edgar_crawler.constants import SEC_HOSTNAME
from edgar_crawler.items import FileDownloadItem

class FilingFileSpider(scrapy.Spider):
    name = "sec-filing-file"
    
    def __init__(self):
        self.db = Database()
        self.conn = self.db.getConn()
        self.cursor = self.conn.cursor()
    
    def start_requests(self):
        yield scrapy.Request(url = SEC_HOSTNAME, callback=self.parse)

    def parse(self, response):
        max_id = 0
        while True:
            self.cursor.execute('''
                SELECT id, doc_link FROM edgar_filing_file 
                WHERE doc_type <> 'GRAPHIC' and doc_name is not null  
                    and description <> 'Complete submission text file' 
                    and doc_name not like '%.xml' and doc_name not like '%.pdf' 
                    and id > {}
                    and doc_link not in (
                        SELECT distinct file_path FROM edgar_file_log where state = 'done'
                    ) limit 10
            '''.format(max_id))
            filesRs = self.cursor.fetchall()
            if len(filesRs) is 0:
                return
            urls = []
            for fileRs in filesRs:
                url = SEC_HOSTNAME + fileRs['doc_link']
                urls.append(url)
                if fileRs['id'] > max_id:
                    max_id = fileRs['id']
            file = FileDownloadItem()
            file['file_urls'] = urls
            yield file
        
        