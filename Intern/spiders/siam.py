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


class siam(scrapy.Spider):

    name = 'siam'
    allowed_domains = ['siamindia.com']
    start_urls = ['http://www.siamindia.com/members.aspx?mpgid=1&pgidtrail=4']

    # rules = [Rule(LinkExtractor(), callback='parse', follow=True)]



    def parse(self, response):

            # url=link

        #url = response.ur

        link= response.xpath("//a[contains(@id,'ctl00_ContentPlaceHolder1_replist')]/@href").extract()
            #print href

        for it in zip(link):
            scraped_info = {'link': it[0]}

            yield scraped_info
