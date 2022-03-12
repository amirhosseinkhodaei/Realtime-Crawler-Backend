import scrapy


class ProductdetailSpider(scrapy.Spider):
    name = 'productdetail'
    start_urls = []


    def parse(self, response):
        data = {}
        attributes = {}
    
        a = []

        product_attr = {}

        product_attr['productName'] = response.css('.row_product_header h1::text').get()
        product_attr['description'] = response.css(".box_comments::text").get()
        for attr in response.css('.box_product_details .tds'):
            attributes[attr.css('.tr div strong::text').get()] = attr.css('.tr .w60::text').get()
         
        a.append(product_attr)
                    
        data['products'] = a
        data['attributes'] = attributes

        yield(data)
