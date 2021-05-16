from edgar_crawler.items import CompanyItem
import scrapy

class CompaniesSpider(scrapy.Spider):
    name = "companies"
    
    def start_requests(self):
        urls = [
            'https://www.sec.gov/cgi-bin/browse-edgar?company=&match=&filenum=&State=&Country=&SIC=6189&myowner=exclude&action=getcompany'
        ]
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)
    
    def parse(self, response):
        url = response.request.url
        print("Start parsing data from page: {}".format(url))
        
        tblRowEles = response.xpath("//div[@id='seriesDiv']/table//tr")
        for rowEle in tblRowEles:
            colEles = rowEle.xpath("./td//text()")
            if len(colEles) < 3:
                continue
            company = CompanyItem()
            company['sic'] = url[url.index('&SIC=')+len('&SIC='): url.index("&myowner")]
            company['cik'] = colEles[0].extract()
            company['company'] = colEles[1].extract()
            company['loc'] = colEles[2].extract()

            yield company
