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


class conpl(scrapy.Spider):

    name = 'conpl'
    allowed_domains = ["constructionplacements.com/75-best-construction-companies-in-india-to-start-your-career-in-2018/"]
    start_urls = ["http://constructionplacements.com/75-best-construction-companies-in-india-to-start-your-career-in-2018/"]

    # rules = [Rule(LinkExtractor(), callback='parse', follow=True)

    def parse(self, response):

            # url=link

        url = response.url
        #email = response.xpath('*//td/text()').re(r'[\w\.-]+@[\w\.-]+')
        web=response.xpath('*//td/a/@href').extract()
        #email = response.xpath('*//p/text()').re(r'[\w\.-]+@[\w\.-]+')
        #email,web=email[31:],web[31:]
        for it in zip(web):
            scraped_info = {'Website URL': it[0]}

            yield scraped_info

                    # filename = response.url.split("/")[-2]
                    # open(filename, 'wb').write(scraped_info)
                    # print((row))

                    # line_count += 1

    