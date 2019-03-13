 #!/usr/bin/python
# -*- coding: utf-8 -*-


# Code to recurse Scrap all weblinks from websites.csv


import csv
import re
import scrapy
import scrapy.item
import xlrd
from scrapy.item import Item, Field
from urllib.parse import urlparse
from urllib.parse import urlsplit
from scrapy.selector import HtmlXPathSelector
import pandas as pd
from scrapy.linkextractors import LinkExtractor

# import scrapy.contrib.linkextractors.sgml

from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor

# from scrapy.contrib.linkextractors.sgml import SgmlLinkExtractor

from scrapy.selector import HtmlXPathSelector


class vae1(scrapy.Spider):

    name = 'vae1'
    allowed_domains = []
    start_urls = []

    # rules = [Rule(LinkExtractor(), callback='parse', follow=True)]

    def __init__(self, filename=None):
        allowed_domains = []
        start_urls = []

        if filename:
            with open(filename, newline='') as f:
                content = csv.reader(f, delimiter=' ')

                for row in content:

                    # row = list(row)

                    self.start_urls.extend(row)

                    # getdom1 = str(row)
                    # getdom1 = getdom1.strip('http://www.')

                    # getdom = list(getdom1)
                    # self.allowed_domains.extend(row)

                    # row+=["//"]

                # print (start_urls)
                # print (allowed_domains)

    def parse(self, response):

            # url=link

        url = response.url
        email = response.xpath('*//a/text()').re(r'[\w\.-]+@+[\w\.-]+')
        web=response.xpath('*//a/@href').re(r'http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+')
        #email = response.xpath('*//p/text()').re(r'[\w\.-]+@[\w\.-]+')
        #email,web=email[31:],web[31:]
        web=list(web)
        if len(web)==0:
            web=[url]
        for it in zip(web,email):
            scraped_info = {'Website URL': it[0],
                            'Email Scraped': it[1]}

            yield scraped_info

                    # filename = response.url.split("/")[-2]
                    # open(filename, 'wb').write(scraped_info)
                    # print((row))

                    # line_count += 1

    