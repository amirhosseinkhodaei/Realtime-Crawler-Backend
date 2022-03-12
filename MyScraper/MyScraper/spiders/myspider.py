import scrapy
# keyword = input('what is the keyword:')


class ThespiderSpider(scrapy.Spider):

    name = 'first'
    start_urls = []

    def parse(self, response):
        products = response.css('.box_product')
        data = {}
        data['paginate'] = {}
    
        a = []
        for products in response.css('.box_product'):

            product_attr = {}

            product_attr['productName'] = products.css('a strong::text').get()
            product_attr['supplier'] = products.css(
                '.name-supplier div:nth-child(2)::text').get()
            product_attr['description'] = products.css('.zone2::text').get()

            # print(product_attr)
            product_attr['url'] = products.css(
                ".box_product a::attr(href)").get()
            a.append(product_attr)
                    
        data['products'] = a
        data['paginate'] = {
            'count': len(response.css(".products-pagination a").getall()) + 1,
            'total': (response.css(".products-count .foro::text").get()).replace("\n", "").replace(" ", "")
        }

        yield(data)
