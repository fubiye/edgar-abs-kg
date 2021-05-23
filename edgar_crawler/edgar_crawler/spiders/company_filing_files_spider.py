
import scrapy
from scrapy.http import request
from edgar_crawler.constants import SEC_HOSTNAME, GET_COMPANY_FILING_TEMP
from edgar_crawler.items import FileDownloadItem, FileDownloadRecordItem, FilingFileItem
# from edgar_crawler.utils import get_query_value
# from edgar_crawler.database import Database

class CompanyFilingSpider(scrapy.Spider):
    name = "filings-file"
    base_domain = SEC_HOSTNAME
    start_urls = [SEC_HOSTNAME]

    def start_requests(self):
        # self.cursor.execute("select distinct cik from edgar_company where cik not in (select distinct cik from edgar_company_filing_craw_log where state = 'done')")
        # ciksRs = self.cursor.fetchall()
        # for cikRs in ciksRs:
        #     url = SEC_HOSTNAME + GET_COMPANY_FILING_TEMP.format(cikRs['cik'], "0")
        url = SEC_HOSTNAME + '/Archives/edgar/data/762153/000153949712000382/0001539497-12-000382-index.htm'
        request = scrapy.Request(url = url, callback=self.parse)
        request.meta['filingID'] = 4315
        yield request
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
        record['state'] = 'start'
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
