import re
import scrapy
import xlrd 

class vae(scrapy.Spider):

    name = 'vae'
    allowed_domains = ["plastemart.com/manufacturers-plastics-machines-compounds-plastics-packaging-products/"]
    start_urls = ["https://vae.ahk.de/en/members/members-directory/?tx_cpsfmp_companymainplugin%5Bpage%5D=1&tx_cpsfmp_companymainplugin%5Bcontroller%5D=Company&cHash=015f1443ba19145ff4415c52c4040c3b",
                  "https://vae.ahk.de/en/members/members-directory/?tx_cpsfmp_companymainplugin%5Bpage%5D=2&tx_cpsfmp_companymainplugin%5Bcontroller%5D=Company&cHash=015f1443ba19145ff4415c52c4040c3b",
                  "https://vae.ahk.de/en/members/members-directory/?tx_cpsfmp_companymainplugin%5Bpage%5D=3&tx_cpsfmp_companymainplugin%5Bcontroller%5D=Company&cHash=015f1443ba19145ff4415c52c4040c3b",
                  "https://vae.ahk.de/en/members/members-directory/?tx_cpsfmp_companymainplugin%5Bpage%5D=4&tx_cpsfmp_companymainplugin%5Bcontroller%5D=Company&cHash=015f1443ba19145ff4415c52c4040c3b",
                  "https://vae.ahk.de/en/members/members-directory/?tx_cpsfmp_companymainplugin%5Bpage%5D=5&tx_cpsfmp_companymainplugin%5Bcontroller%5D=Company&cHash=015f1443ba19145ff4415c52c4040c3b",
                  "https://vae.ahk.de/en/members/members-directory/?tx_cpsfmp_companymainplugin%5Bpage%5D=6&tx_cpsfmp_companymainplugin%5Bcontroller%5D=Company&cHash=015f1443ba19145ff4415c52c4040c3b",
                  "https://vae.ahk.de/en/members/members-directory/?tx_cpsfmp_companymainplugin%5Bpage%5D=7&tx_cpsfmp_companymainplugin%5Bcontroller%5D=Company&cHash=015f1443ba19145ff4415c52c4040c3b",
                  "https://vae.ahk.de/en/members/members-directory/?tx_cpsfmp_companymainplugin%5Bpage%5D=8&tx_cpsfmp_companymainplugin%5Bcontroller%5D=Company&cHash=015f1443ba19145ff4415c52c4040c3b",
                  "https://vae.ahk.de/en/members/members-directory/?tx_cpsfmp_companymainplugin%5Bpage%5D=9&tx_cpsfmp_companymainplugin%5Bcontroller%5D=Company&cHash=015f1443ba19145ff4415c52c4040c3b",
                  "https://vae.ahk.de/en/members/members-directory/?tx_cpsfmp_companymainplugin%5Bpage%5D=10&tx_cpsfmp_companymainplugin%5Bcontroller%5D=Company&cHash=015f1443ba19145ff4415c52c4040c3b",
                  "https://vae.ahk.de/en/members/members-directory/?tx_cpsfmp_companymainplugin%5Bpage%5D=10&tx_cpsfmp_companymainplugin%5Bcontroller%5D=Company&cHash=015f1443ba19145ff4415c52c4040c3b",
                  "https://vae.ahk.de/en/members/members-directory/?tx_cpsfmp_companymainplugin%5Bpage%5D=12&tx_cpsfmp_companymainplugin%5Bcontroller%5D=Company&cHash=015f1443ba19145ff4415c52c4040c3b",
                  "https://vae.ahk.de/en/members/members-directory/?tx_cpsfmp_companymainplugin%5Bpage%5D=13&tx_cpsfmp_companymainplugin%5Bcontroller%5D=Company&cHash=015f1443ba19145ff4415c52c4040c3b",
                  "https://vae.ahk.de/en/members/members-directory/?tx_cpsfmp_companymainplugin%5Bpage%5D=14&tx_cpsfmp_companymainplugin%5Bcontroller%5D=Company&cHash=015f1443ba19145ff4415c52c4040c3b",
                  "https://vae.ahk.de/en/members/members-directory/?tx_cpsfmp_companymainplugin%5Bpage%5D=15&tx_cpsfmp_companymainplugin%5Bcontroller%5D=Company&cHash=015f1443ba19145ff4415c52c4040c3b",
                  "https://vae.ahk.de/en/members/members-directory/?tx_cpsfmp_companymainplugin%5Bpage%5D=16&tx_cpsfmp_companymainplugin%5Bcontroller%5D=Company&cHash=015f1443ba19145ff4415c52c4040c3b",
                  "https://vae.ahk.de/en/members/members-directory/?tx_cpsfmp_companymainplugin%5Bpage%5D=17&tx_cpsfmp_companymainplugin%5Bcontroller%5D=Company&cHash=015f1443ba19145ff4415c52c4040c3b",
                  "https://vae.ahk.de/en/members/members-directory/?tx_cpsfmp_companymainplugin%5Bpage%5D=18&tx_cpsfmp_companymainplugin%5Bcontroller%5D=Company&cHash=015f1443ba19145ff4415c52c4040c3b",
                  "https://vae.ahk.de/en/members/members-directory/?tx_cpsfmp_companymainplugin%5Bpage%5D=19&tx_cpsfmp_companymainplugin%5Bcontroller%5D=Company&cHash=015f1443ba19145ff4415c52c4040c3b",
                  "https://vae.ahk.de/en/members/members-directory/?tx_cpsfmp_companymainplugin%5Bpage%5D=20&tx_cpsfmp_companymainplugin%5Bcontroller%5D=Company&cHash=015f1443ba19145ff4415c52c4040c3b",
                  "https://vae.ahk.de/en/members/members-directory/?tx_cpsfmp_companymainplugin%5Bpage%5D=21&tx_cpsfmp_companymainplugin%5Bcontroller%5D=Company&cHash=015f1443ba19145ff4415c52c4040c3b",
                  "https://vae.ahk.de/en/members/members-directory/?tx_cpsfmp_companymainplugin%5Bpage%5D=22&tx_cpsfmp_companymainplugin%5Bcontroller%5D=Company&cHash=015f1443ba19145ff4415c52c4040c3b",
                  "https://vae.ahk.de/en/members/members-directory/?tx_cpsfmp_companymainplugin%5Bpage%5D=23&tx_cpsfmp_companymainplugin%5Bcontroller%5D=Company&cHash=015f1443ba19145ff4415c52c4040c3b",
                  "https://vae.ahk.de/en/members/members-directory/?tx_cpsfmp_companymainplugin%5Bpage%5D=24&tx_cpsfmp_companymainplugin%5Bcontroller%5D=Company&cHash=015f1443ba19145ff4415c52c4040c3b",
                  "https://vae.ahk.de/en/members/members-directory/?tx_cpsfmp_companymainplugin%5Bpage%5D=25&tx_cpsfmp_companymainplugin%5Bcontroller%5D=Company&cHash=015f1443ba19145ff4415c52c4040c3b",
                  "https://vae.ahk.de/en/members/members-directory/?tx_cpsfmp_companymainplugin%5Bpage%5D=26&tx_cpsfmp_companymainplugin%5Bcontroller%5D=Company&cHash=015f1443ba19145ff4415c52c4040c3b",
                  "https://vae.ahk.de/en/members/members-directory/?tx_cpsfmp_companymainplugin%5Bpage%5D=27&tx_cpsfmp_companymainplugin%5Bcontroller%5D=Company&cHash=015f1443ba19145ff4415c52c4040c3b",
                  "https://vae.ahk.de/en/members/members-directory/?tx_cpsfmp_companymainplugin%5Bpage%5D=28&tx_cpsfmp_companymainplugin%5Bcontroller%5D=Company&cHash=015f1443ba19145ff4415c52c4040c3b",
                  "https://vae.ahk.de/en/members/members-directory/?tx_cpsfmp_companymainplugin%5Bpage%5D=29&tx_cpsfmp_companymainplugin%5Bcontroller%5D=Company&cHash=015f1443ba19145ff4415c52c4040c3b",
                  "https://vae.ahk.de/en/members/members-directory/?tx_cpsfmp_companymainplugin%5Bpage%5D=30&tx_cpsfmp_companymainplugin%5Bcontroller%5D=Company&cHash=015f1443ba19145ff4415c52c4040c3b",
                  "https://vae.ahk.de/en/members/members-directory/?tx_cpsfmp_companymainplugin%5Bpage%5D=31&tx_cpsfmp_companymainplugin%5Bcontroller%5D=Company&cHash=015f1443ba19145ff4415c52c4040c3b",
                  "https://vae.ahk.de/en/members/members-directory/?tx_cpsfmp_companymainplugin%5Bpage%5D=32&tx_cpsfmp_companymainplugin%5Bcontroller%5D=Company&cHash=015f1443ba19145ff4415c52c4040c3b",
                  "https://vae.ahk.de/en/members/members-directory/?tx_cpsfmp_companymainplugin%5Bpage%5D=33&tx_cpsfmp_companymainplugin%5Bcontroller%5D=Company&cHash=015f1443ba19145ff4415c52c4040c3b",
                  "https://vae.ahk.de/en/members/members-directory/?tx_cpsfmp_companymainplugin%5Bpage%5D=34&tx_cpsfmp_companymainplugin%5Bcontroller%5D=Company&cHash=015f1443ba19145ff4415c52c4040c3b",
                  "https://vae.ahk.de/en/members/members-directory/?tx_cpsfmp_companymainplugin%5Bpage%5D=35&tx_cpsfmp_companymainplugin%5Bcontroller%5D=Company&cHash=015f1443ba19145ff4415c52c4040c3b",
                  "https://vae.ahk.de/en/members/members-directory/?tx_cpsfmp_companymainplugin%5Bpage%5D=36&tx_cpsfmp_companymainplugin%5Bcontroller%5D=Company&cHash=015f1443ba19145ff4415c52c4040c3b",
                  "https://vae.ahk.de/en/members/members-directory/?tx_cpsfmp_companymainplugin%5Bpage%5D=37&tx_cpsfmp_companymainplugin%5Bcontroller%5D=Company&cHash=015f1443ba19145ff4415c52c4040c3b",
                  "https://vae.ahk.de/en/members/members-directory/?tx_cpsfmp_companymainplugin%5Bpage%5D=38&tx_cpsfmp_companymainplugin%5Bcontroller%5D=Company&cHash=015f1443ba19145ff4415c52c4040c3b",
                  "https://vae.ahk.de/en/members/members-directory/?tx_cpsfmp_companymainplugin%5Bpage%5D=39&tx_cpsfmp_companymainplugin%5Bcontroller%5D=Company&cHash=015f1443ba19145ff4415c52c4040c3b",
                  "https://vae.ahk.de/en/members/members-directory/?tx_cpsfmp_companymainplugin%5Bpage%5D=40&tx_cpsfmp_companymainplugin%5Bcontroller%5D=Company&cHash=015f1443ba19145ff4415c52c4040c3b",
                  "https://vae.ahk.de/en/members/members-directory/?tx_cpsfmp_companymainplugin%5Bpage%5D=41&tx_cpsfmp_companymainplugin%5Bcontroller%5D=Company&cHash=015f1443ba19145ff4415c52c4040c3b",
                  "https://vae.ahk.de/en/members/members-directory/?tx_cpsfmp_companymainplugin%5Bpage%5D=42&tx_cpsfmp_companymainplugin%5Bcontroller%5D=Company&cHash=015f1443ba19145ff4415c52c4040c3b",
                  "https://vae.ahk.de/en/members/members-directory/?tx_cpsfmp_companymainplugin%5Bpage%5D=43&tx_cpsfmp_companymainplugin%5Bcontroller%5D=Company&cHash=015f1443ba19145ff4415c52c4040c3b",
                  "https://vae.ahk.de/en/members/members-directory/?tx_cpsfmp_companymainplugin%5Bpage%5D=44&tx_cpsfmp_companymainplugin%5Bcontroller%5D=Company&cHash=015f1443ba19145ff4415c52c4040c3b",
                  "https://vae.ahk.de/en/members/members-directory/?tx_cpsfmp_companymainplugin%5Bpage%5D=45&tx_cpsfmp_companymainplugin%5Bcontroller%5D=Company&cHash=015f1443ba19145ff4415c52c4040c3b",
                  "https://vae.ahk.de/en/members/members-directory/?tx_cpsfmp_companymainplugin%5Bpage%5D=46&tx_cpsfmp_companymainplugin%5Bcontroller%5D=Company&cHash=015f1443ba19145ff4415c52c4040c3b",
                  "https://vae.ahk.de/en/members/members-directory/?tx_cpsfmp_companymainplugin%5Bpage%5D=47&tx_cpsfmp_companymainplugin%5Bcontroller%5D=Company&cHash=015f1443ba19145ff4415c52c4040c3b",
                  "https://vae.ahk.de/en/members/members-directory/?tx_cpsfmp_companymainplugin%5Bpage%5D=48&tx_cpsfmp_companymainplugin%5Bcontroller%5D=Company&cHash=015f1443ba19145ff4415c52c4040c3b",
                  "https://vae.ahk.de/en/members/members-directory/?tx_cpsfmp_companymainplugin%5Bpage%5D=49&tx_cpsfmp_companymainplugin%5Bcontroller%5D=Company&cHash=015f1443ba19145ff4415c52c4040c3b",
                  "https://vae.ahk.de/en/members/members-directory/?tx_cpsfmp_companymainplugin%5Bpage%5D=50&tx_cpsfmp_companymainplugin%5Bcontroller%5D=Company&cHash=015f1443ba19145ff4415c52c4040c3b",
                  "https://vae.ahk.de/en/members/members-directory/?tx_cpsfmp_companymainplugin%5Bpage%5D=51&tx_cpsfmp_companymainplugin%5Bcontroller%5D=Company&cHash=015f1443ba19145ff4415c52c4040c3b",
                  "https://vae.ahk.de/en/members/members-directory/?tx_cpsfmp_companymainplugin%5Bpage%5D=52&tx_cpsfmp_companymainplugin%5Bcontroller%5D=Company&cHash=015f1443ba19145ff4415c52c4040c3b",

                    

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
