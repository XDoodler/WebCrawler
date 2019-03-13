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


class geek(scrapy.Spider):

    name = 'geek'
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
        email = response.xpath('*//a/text()').re(r'[\w\.-]+@[\w\.-]+')
            #print href

        for it in zip(email):
            result = url
            #result = \
             #   '{uri.scheme}://{uri.netloc}/'.format(uri=parsed_uri)
            scraped_info = {'link': result,
                            'email': it[0]}

            yield scraped_info
