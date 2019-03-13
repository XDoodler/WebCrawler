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


class linker(scrapy.Spider):

    name = 'linker'
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

    def parse_item(self, response):

            # url=link

        url = response.url
        email = response.xpath('*//a/text()').re(r'[\w\.-]+@[\w\.-]+')
        #email = response.xpath('*//p/text()').re(r'[\w\.-]+@[\w\.-]+')
        email = list(email)
        if len(email) == 0:
            email = ['']  # check whether the email is fetched or not

        for it in zip(email):
            parsed_uri = urlparse(url)
            result = \
                '{uri.scheme}://{uri.netloc}/'.format(uri=parsed_uri)
            scraped_info = {'Website URL': result,
                            'Email Scraped': it[0]}

            yield scraped_info

                    # filename = response.url.split("/")[-2]
                    # open(filename, 'wb').write(scraped_info)
                    # print((row))

                    # line_count += 1

    def parse(self, response):

                    # start_urls = 'http://' + row[i]
                    # print(allowed_domains)
                    # filename = response.url.split("/")[-2]
                    # for i in range(333):

        # print (response.request.url)

        # email = Field(default='Not found')

        # url = response.url

        hxs = scrapy.Selector(response)

        # extract all links from page

        all_links = hxs.xpath('*//a/@href').extract()

        # iterate over links
        parsed_uri = urlparse(response.url)
        result = \
                '{uri.scheme}://{uri.netloc}/'.format(uri=parsed_uri)
        for link in all_links:
            checker = str(link)
            if result  not in checker :
                #dup_url = str(response.url)
                #if dup_url[len(dup_url) - 1] == '/':
                    #checker = checker[1:]
                link = str(str(response.url)+"/"+ checker)
            else:
                link=checker    

            yield scrapy.http.Request(url=link,
                    callback=self.parse_item)


        # hxs = HtmlXPathSelector(response)

        # result = '{uri.scheme}://{uri.netloc}/'.format(uri=parsed_uri)
        # domain=parsed_uri.geturl()
        # name = response.xpath('//title/text()').extract()

        # email = hxs.xpath('//body'
                          # ).re(r'([a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+.[a-zA-Z0-9-.]+)'
                               # )

        # email = response.xpath('//p/text()').re(r'[\w\.-]+@[\w\.-]+')

        # email = response.xpath('//a/text()').re(r"[a-z0-9\.\-+_]+@[a-z0-9\.\-+_]+\.[a-z]+")
        # email = response.xpath('//a/@href').re(r"[a-z0-9\.\-+_]+@[a-z0-9\.\-+_]+\.[a-z]+")
        # email = response.xpath('//footer').re(r'[\w\.-]+@[\w\.-]+')


			