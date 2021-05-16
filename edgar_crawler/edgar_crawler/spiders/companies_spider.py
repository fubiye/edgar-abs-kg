from edgar_crawler.items import CompanyItem
import scrapy

def LastNlines(fname, N):
      
    # assert statement check
    # a condition
    assert N >= 0
      
    # declaring variable
    # to implement 
    # exponential search
    pos = N + 1
      
    # list to store
    # last N lines
    lines = []
      
    # opening file using with() method
    # so that file get closed
    # after completing work
    with open(fname) as f:
          
        # loop which runs
        # until size of list
        # becomes equal to N
        while len(lines) <= N:
              
            # try block
            try:
                # moving cursor from
                # left side to
                # pos line from end
                f.seek(-pos, 2)
          
            # exception block 
            # to hadle any run 
            # time error
            except IOError:
                f.seek(0)
                break
              
            # finally block 
            # to add lines 
            # to list after
            # each iteration
            finally:
                lines = list(f)
              
            # increasing value
            # of variable
            # exponentially
            pos *= 2
              
    # returning the
    # whole list
    # which stores last
    # N lines
    return lines[-N:]

SEC_HOSTNAME = 'https://www.sec.gov'
STATUS_SAVE_POINT = 'save_point'
class CompaniesSpider(scrapy.Spider):
    name = "companies"
    
    def start_requests(self):
        lastLine = LastNlines(STATUS_SAVE_POINT, 1)[0]
        lastStart = lastLine[:lastLine.index("\n")]
        urls = [
            SEC_HOSTNAME + '/cgi-bin/browse-edgar?action=getcompany&SIC=6189&owner=include&match=&start=' + lastStart + '&count=40&hidefilings=0'
        ]
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)
    
    def parse(self, response):
        url = response.request.url
        print("Start parsing data from page: {}".format(url))
        self.save_status(url)
        tblRowEles = response.xpath("//div[@id='seriesDiv']/table//tr")
        for rowEle in tblRowEles:
            colEles = rowEle.xpath("./td//text()")
            if len(colEles) < 3:
                continue
            company = CompanyItem()
            company['sic'] = url[url.index('&SIC=')+len('&SIC='): url.index("&owner")]
            company['cik'] = colEles[0].extract()
            company['company'] = colEles[1].extract()
            company['loc'] = colEles[2].extract()

            yield company
        onclickEle = response.xpath("//form/input[contains(@value,'Next')]//@onclick")
        if len(onclickEle) is 0:
            return
        onclick = onclickEle.extract_first()
        nextUrl = onclick[onclick.index("parent.location='")+len("parent.location='"):-1]
        yield scrapy.Request(url=SEC_HOSTNAME+nextUrl, callback=self.parse)
    def save_status(self, url):
        if url.index('start=') < 0:
            return
        start = url[url.index('start=')+len('start='):url.index('&count=')]
        with open('save_point','a') as file:
            file.write(start)
            file.write("\n")

