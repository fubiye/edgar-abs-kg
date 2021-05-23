
import scrapy
from edgar_crawler.constants import SEC_HOSTNAME, GET_COMPANY_FILING_TEMP
from edgar_crawler.items import FileDownloadItem, FileDownloadRecordItem
# from edgar_crawler.utils import get_query_value
# from edgar_crawler.database import Database

class CompanyFilingSpider(scrapy.Spider):
    name = "filings-file"
    base_domain = SEC_HOSTNAME
    start_urls = [SEC_HOSTNAME]
    def parse(self, response):
        file = FileDownloadItem()
        file['file_urls'] = [SEC_HOSTNAME + '/Archives/edgar/data/762153/000153949712000382/0001539497-12-000382-index.htm']
        yield file
        record = FileDownloadRecordItem()
        record['path'] = '/Archives/edgar/data/762153/000153949712000382/0001539497-12-000382-index.htm'
        record['state'] = 'start'
        yield record