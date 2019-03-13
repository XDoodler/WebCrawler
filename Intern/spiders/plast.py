import re
import scrapy
import xlrd 

class plast(scrapy.Spider):

    name = 'plast'
    allowed_domains = ["plastemart.com/manufacturers-plastics-machines-compounds-plastics-packaging-products/"]
    start_urls = ["http://www.plastemart.com/manufacturers-plastics-machines-compounds-plastics-packaging-products/2",
                 "http://www.plastemart.com/manufacturers-plastics-machines-compounds-plastics-packaging-products/3",
                 "http://www.plastemart.com/manufacturers-plastics-machines-compounds-plastics-packaging-products/4"
                 "http://www.plastemart.com/manufacturers-plastics-machines-compounds-plastics-packaging-products/5"
                 "http://www.plastemart.com/manufacturers-plastics-machines-compounds-plastics-packaging-products/6",
                 "http://www.plastemart.com/manufacturers-plastics-machines-compounds-plastics-packaging-products/7",
                 "http://www.plastemart.com/manufacturers-plastics-machines-compounds-plastics-packaging-products/8",
                 "http://www.plastemart.com/manufacturers-plastics-machines-compounds-plastics-packaging-products/9",
                 "http://www.plastemart.com/manufacturers-plastics-machines-compounds-plastics-packaging-products/10",
                 "http://www.plastemart.com/manufacturers-plastics-machines-compounds-plastics-packaging-products/11",
                 "http://www.plastemart.com/manufacturers-plastics-machines-compounds-plastics-packaging-products/12",
                 "http://www.plastemart.com/manufacturers-plastics-machines-compounds-plastics-packaging-products/13",
                 "http://www.plastemart.com/manufacturers-plastics-machines-compounds-plastics-packaging-products/14",
                 "http://www.plastemart.com/manufacturers-plastics-machines-compounds-plastics-packaging-products/15",
                 "http://www.plastemart.com/manufacturers-plastics-machines-compounds-plastics-packaging-products/16",
                 "http://www.plastemart.com/manufacturers-plastics-machines-compounds-plastics-packaging-products/17",
                 "http://www.plastemart.com/manufacturers-plastics-machines-compounds-plastics-packaging-products/18",
                 "http://www.plastemart.com/manufacturers-plastics-machines-compounds-plastics-packaging-products/19",
                 "http://www.plastemart.com/manufacturers-plastics-machines-compounds-plastics-packaging-products/20",
                 "http://www.plastemart.com/manufacturers-plastics-machines-compounds-plastics-packaging-products/21",
                 "http://www.plastemart.com/manufacturers-plastics-machines-compounds-plastics-packaging-products/22",
                 "http://www.plastemart.com/manufacturers-plastics-machines-compounds-plastics-packaging-products/23",
                 "http://www.plastemart.com/manufacturers-plastics-machines-compounds-plastics-packaging-products/24",
                 "http://www.plastemart.com/manufacturers-plastics-machines-compounds-plastics-packaging-products/25",
                 "http://www.plastemart.com/manufacturers-plastics-machines-compounds-plastics-packaging-products/26"
                 ]

    def parse(self, response):

            # Extracting the content using css selectors
        #links={
            link=response.xpath('*//td/a/@href').extract()
        
        #name=response.xpath('//title/text()').extract_first()
        #email=response.xpath('//p/text()').re_first(r'[\w\.-]+@[\w\.-]+')
            for item in zip(link):
            #create a dictionary to store the scraped info
                info = {
                #'Website name': item[0],
                #'Contact': item[1],
                "Links":item[0]
                }
                yield info
