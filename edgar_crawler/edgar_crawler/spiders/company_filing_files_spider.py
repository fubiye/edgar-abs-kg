
from time import sleep
import scrapy
from scrapy.http import request
from edgar_crawler.constants import SEC_HOSTNAME, GET_COMPANY_FILING_TEMP
from edgar_crawler.items import FileDownloadItem, FileDownloadRecordItem, FilingFileItem
# from edgar_crawler.utils import get_query_value
from edgar_crawler.database import Database

class CompanyFilingSpider(scrapy.Spider):
    name = "filings-file"
    base_domain = SEC_HOSTNAME
    start_urls = [SEC_HOSTNAME]

    def __init__(self):
        self.db = Database()
        self.conn = self.db.getConn()
        self.cursor = self.conn.cursor()

    def start_requests(self):
        max_id = 0
        while True:
            self.cursor.execute('''select id, docs_link from edgar_company_filing where id > {} and docs_link not in (
                                        SELECT distinct file_path FROM edgar_file_log where state = 'done'
                                    ) limit 20'''.format(max_id))
            filingsRs = self.cursor.fetchall()
            if len(filingsRs) is 0:
                return
            for filingRs in filingsRs:
                url = SEC_HOSTNAME + filingRs['docs_link']
                request = scrapy.Request(url = url, callback=self.parse)
                filingID = filingRs['id']
                if filingID > max_id:
                    max_id = filingID
                request.meta['filingID'] = filingID
                yield request
            sleep(10)
    def parse(self, response):
        url = response.request.url
        filingID = response.request.meta['filingID']
        path = url[len(SEC_HOSTNAME):]
        file = FileDownloadItem()
        file['file_urls'] = [
            url
        ]
        yield file
        record = FileDownloadRecordItem()
        record['path'] = path
        record['state'] = 'done'
        yield record
        tblRowEles = response.xpath("//table[@class='tableFile']//tr")
        for rowEle in tblRowEles:
            colEles = rowEle.xpath("./td")
            if len(colEles) < 5:
                continue
            file = FilingFileItem()
            file['filing_id'] = filingID
            file['seq'] = colEles[0].xpath('.//text()').extract_first()
            file['description'] = colEles[1].xpath(".//text()").extract_first()
            file['doc_name'] = colEles[2].xpath(".//text()").extract_first()
            file['doc_link'] = colEles[2].xpath("./a/@href").extract_first()
            file['doc_type'] = colEles[3].xpath(".//text()").extract_first()
            file['size'] = colEles[4].xpath(".//text()").extract_first()
            yield file
