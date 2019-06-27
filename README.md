# WebCrawler

This software was developed while I was an Intern at Intellinet Systems Pvt. Ltd. [ https://www.intellinetsystem.com ].
It is based on Scrapy (a free and open-source web-crawling framework written in Python. Originally designed for web scraping, it can also be used to extract data using APIs or as a general-purpose web crawler. It is currently maintained by Scrapinghub Ltd., a web-scraping development and services company) and uses Customized Spiders/bots designed to fetch Contacts and other informations from their Exhibitors.

# Customized Spiders for Data Extraction



## Installation

Use the [Installation Guide to Scrapy](http://doc.scrapy.org/en/latest/intro/install.html) to install Scrapy and build your environment to start designing customized spiders.

```bash
import scrapy
```

## Imports

```python
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

```

## Custom Spiders
These Customized spiders were built after a complete analysis of the websites, their architectures and scraping the entire footer of the website to get emails and contacts.

## Snippet to Scrap Multiple links stored in text file

This snippet takes care of scraping multiple websites from a file that are listed down in it.

```python
class name_of_your_spider(scrapy.Spider):

    name = 'name_of_your_spider'
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

                    self.start_urls.extend(row)

```


## Snippet to Scrap multiple webpages of a website

```python
for link in all_links:
            checker = str(link)
            link = str(str(response.url)+ checker)   

            yield scrapy.http.Request(url=link,
                    callback=self.parse_item,dont_filter = True)
```

#### Define a special Function to handle this


```python
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

```

## Reports 

The Reports are now open-sourced :)

## Demonstration
[Video Explanation](https://www.youtube.com/watch?v=TYzriTq9hZc&t=119s)
