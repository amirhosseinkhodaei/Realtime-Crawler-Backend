import scrapy


class AllproductsSpider(scrapy.Spider):
    name = 'allProducts'
    allowed_domains = ['a.com']
    start_urls = ['http://a.com/']

    def parse(self, response):
        pass
