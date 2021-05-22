
import scrapy
from edgar_crawler.constants import SEC_HOSTNAME, GET_COMPANY_FILING_TEMP
from edgar_crawler.items import CompanyFilingItem, CompanyFilingStateItem
from edgar_crawler.utils import get_query_value
class CompanyFilingSpider(scrapy.Spider):
    name = "filings"

    def start_requests(self):
        url = SEC_HOSTNAME + GET_COMPANY_FILING_TEMP.format("0000020164", "0")
        yield scrapy.Request(url = url, callback=self.parse)

    def parse(self, response):
        url = response.request.url
        print("Start parsing data from page: {}".format(url))
        cik = get_query_value(url,'CIK','type')
        tblRowEles = response.xpath("//div[@id='seriesDiv']/table//tr")
        
        for rowEle in tblRowEles:
            colEles = rowEle.xpath("./td")
            if len(colEles) < 5:
                continue
            filing = CompanyFilingItem()
            filing['cik'] = cik
            filing['filing'] = colEles[0].xpath('.//text()').extract_first()
            filing['docs_link'] = colEles[1].xpath("./a/@href").extract_first()
            filing['filing_desc'] = "\n".join(colEles[2].xpath(".//text()").extract())
            filing['effective'] = colEles[3].xpath(".//text()").extract_first()
            filing['file_num'] = colEles[4].xpath("./a/text()").extract_first()
            filing['file_num_raw'] = "\n".join(colEles[4].xpath(".//text()").extract())
            yield filing
        
        stateItem = CompanyFilingStateItem()
        stateItem['cik'] = cik
        stateItem['category'] = 1

        onclickEle = response.xpath("//form//input[contains(@value,'Next')]//@onclick")
        if len(onclickEle) is 0:
            stateItem['state'] = 'done'
            yield stateItem
            return
        stateItem['state'] = 'crawl'
        yield stateItem

        onclick = onclickEle.extract_first()
        nextUrl = onclick[onclick.index("parent.location='")+len("parent.location='"):-1]
        yield scrapy.Request(url=SEC_HOSTNAME+nextUrl, callback=self.parse)
        
        