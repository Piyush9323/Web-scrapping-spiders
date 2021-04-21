# AUTHOR : PIYUSH SHARMA (2020PCS1014)
# Using multiple user agents to bypass restrictions

import scrapy
from ..items import WebCrawlItem


class AmazonSpider(scrapy.Spider):
    name = 'amazon'

    start_urls = [
    'https://www.amazon.com/s?bbn=283155&rh=n%3A283155%2Cp_n_publication_date%3A1250226011&dc&qid=1607700113&rnid=1250225011&ref=lp_1000_nr_p_n_publication_date_0'
    ]

    def parse(self, response): 
        items = WebCrawlItem()
        product_name = response.css('.a-color-base.a-text-normal::text').extract()
        product_author = response.css('.a-color-secondary .a-size-base.a-link-normal').css('::text').extract()
        product_price = response.css('.a-price-whole::text').extract()
        product_imagelink = response.css('.s-image::attr(src)').extract()

        items['product_name'] = product_name
        items['product_author'] = product_author
        items['product_price'] = product_price
        items['product_imagelink'] = product_imagelink

        yield items

        pass
