#!/usr/bin/python
# -*- coding: utf-8 -*-

# author : Soham Chakrabarti 
#date : 25.11.2018


#Code Documentation :


#The Basic idea behind this approach is make this code as simple as possible with low complexity and time consumption.
#The following snippet is powerful and can be executed by off-commening any one single of those code lines from (37 - 43)
#The main task is to study the architecture and execute using css selectors. I am really experienced in this and so it took me 15 minutes.


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
from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor
from scrapy.selector import HtmlXPathSelector


class hindu(scrapy.Spider):

    name = 'hindu'
    allowed_domains = ['hindustantimes.com']
    start_urls = ['http://www.hindustantimes.com/']

    def parse(self, response):
        #news= response.xpath("//div[contains(@class,'subhead4')]/h2/a/text()").extract()
        #news= response.xpath("//div[@class='subhead4 ']/a/h2/text()").extract()
        #news= response.xpath("//div[contains(@class,'para-txt')]/a/text()").extract()
        #news= response.xpath("//div[contains(@class,'para-txt')]/a/text()").extract()
        #news= response.xpath("//div[contains(@class,'heading4')]/a/text()").extract()
        #news= response.xpath("//div[contains(@class,'heading5')]/a/text()").extract()
        for i in zip(news):
            scraped_info = {'link': i[0]}

            yield scraped_info
