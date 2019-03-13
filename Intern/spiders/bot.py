#!/usr/bin/python
# -*- coding: utf-8 -*-

# Code to Scrap out all the Websites from www.10times.com/equipmag-expo/exhibitors/

#Code starts
import re
import scrapy
import xlrd 

class bot(scrapy.Spider):

    name = 'bot'
    allowed_domains = ["www.india.gov.in/topics/travel-tourism/approved-agents"]
    start_urls = ["https://www.india.gov.in/topics/travel-tourism/approved-agents"]

    def parse(self, response):

            # Extracting the content using css selectors
        #links={
            link=response.xpath('*//a/link()').re(r'[\w\.-]+@[\w\.-]+')
            #}

        
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



            