import re
import scrapy
import xlrd 

class impa(scrapy.Spider):

    name = 'impa'
    allowed_domains = ["impa.net/members-directory/all/all/"]
    start_urls = ["https://impa.net/members-directory/all/all/p1/",
                  "https://impa.net/members-directory/all/all/p2/",
                  "https://impa.net/members-directory/all/all/p3/",
                  "https://impa.net/members-directory/all/all/p4/",
                  "https://impa.net/members-directory/all/all/p5/",
                  "https://impa.net/members-directory/all/all/p6/",
                  "https://impa.net/members-directory/all/all/p7/",
                  "https://impa.net/members-directory/all/all/p8/",
                  "https://impa.net/members-directory/all/all/p9/",
                  "https://impa.net/members-directory/all/all/p10/",
                  "https://impa.net/members-directory/all/all/p11/",
                  "https://impa.net/members-directory/all/all/p12/",
                  "https://impa.net/members-directory/all/all/p13/",
                  "https://impa.net/members-directory/all/all/p14/",
                  "https://impa.net/members-directory/all/all/p15/",
                  "https://impa.net/members-directory/all/all/p16/",
                  "https://impa.net/members-directory/all/all/p17/",
                  "https://impa.net/members-directory/all/all/p18/",
                  "https://impa.net/members-directory/all/all/p19/",
                  "https://impa.net/members-directory/all/all/p20/",
                  "https://impa.net/members-directory/all/all/p21/",
                  "https://impa.net/members-directory/all/all/p22/",
                  "https://impa.net/members-directory/all/all/p23/",
                  "https://impa.net/members-directory/all/all/p24/",
                  "https://impa.net/members-directory/all/all/p25/",
                  "https://impa.net/members-directory/all/all/p26/",
                  "https://impa.net/members-directory/all/all/p27/",
                  "https://impa.net/members-directory/all/all/p28/",
                  "https://impa.net/members-directory/all/all/p29/",
                  "https://impa.net/members-directory/all/all/p30/",
                  "https://impa.net/members-directory/all/all/p31/",
                  "https://impa.net/members-directory/all/all/p32/",
                  "https://impa.net/members-directory/all/all/p33/",
                  "https://impa.net/members-directory/all/all/p34/",
                  "https://impa.net/members-directory/all/all/p35/",
                  "https://impa.net/members-directory/all/all/p36/",
                  "https://impa.net/members-directory/all/all/p37/",
                  "https://impa.net/members-directory/all/all/p38/",
                  "https://impa.net/members-directory/all/all/p39/",
                  "https://impa.net/members-directory/all/all/p40/",
                  "https://impa.net/members-directory/all/all/p41/",
                  "https://impa.net/members-directory/all/all/p42/",
                  "https://impa.net/members-directory/all/all/p43/",
                  "https://impa.net/members-directory/all/all/p44/",
                  "https://impa.net/members-directory/all/all/p45/",
                  "https://impa.net/members-directory/all/all/p46/",
                  "https://impa.net/members-directory/all/all/p47/",
                  "https://impa.net/members-directory/all/all/p48/",
                  "https://impa.net/members-directory/all/all/p49/",
                  "https://impa.net/members-directory/all/all/p50/",
                  "https://impa.net/members-directory/all/all/p51/",
                  "https://impa.net/members-directory/all/all/p52/",
                  "https://impa.net/members-directory/all/all/p53/",
                  "https://impa.net/members-directory/all/all/p54/",
                  "https://impa.net/members-directory/all/all/p55/",
                  "https://impa.net/members-directory/all/all/p56/",
                  "https://impa.net/members-directory/all/all/p57/",
                  "https://impa.net/members-directory/all/all/p58/",
                  "https://impa.net/members-directory/all/all/p59/",
                  "https://impa.net/members-directory/all/all/p60/",
                  "https://impa.net/members-directory/all/all/p61/",
                  "https://impa.net/members-directory/all/all/p62/",
                  "https://impa.net/members-directory/all/all/p63/",
                  "https://impa.net/members-directory/all/all/p64/",
                  "https://impa.net/members-directory/all/all/p65/",
                  "https://impa.net/members-directory/all/all/p66/",
                  "https://impa.net/members-directory/all/all/p67/",
                  "https://impa.net/members-directory/all/all/p68/",
                  "https://impa.net/members-directory/all/all/p69/",
                  "https://impa.net/members-directory/all/all/p70/",
                  "https://impa.net/members-directory/all/all/p71/",
                  "https://impa.net/members-directory/all/all/p72/",
                  "https://impa.net/members-directory/all/all/p73/",
                  "https://impa.net/members-directory/all/all/p74/",
                  "https://impa.net/members-directory/all/all/p75/",
                  "https://impa.net/members-directory/all/all/p76/",
                  "https://impa.net/members-directory/all/all/p77/",
                  "https://impa.net/members-directory/all/all/p78/",
                  "https://impa.net/members-directory/all/all/p79/",
                  "https://impa.net/members-directory/all/all/p80/",
                  "https://impa.net/members-directory/all/all/p81/",
                  "https://impa.net/members-directory/all/all/p82/",
                  "https://impa.net/members-directory/all/all/p83/",
                  "https://impa.net/members-directory/all/all/p84/",
                  "https://impa.net/members-directory/all/all/p85/",
                  "https://impa.net/members-directory/all/all/p86/",
                  "https://impa.net/members-directory/all/all/p87/",
                  "https://impa.net/members-directory/all/all/p88/",
                  "https://impa.net/members-directory/all/all/p89/",
                  "https://impa.net/members-directory/all/all/p90/",
                  "https://impa.net/members-directory/all/all/p91/",
                 ]

    def parse(self, response):

            # Extracting the content using css selectors
        #links={
            link=response.xpath('*//a[@title="Visit XXX"]/@href').extract()
        
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
