import scrapy


class ApplicationsSpider(scrapy.Spider):
    name = 'applications'
    start_urls = ['https://polymer-additives.specialchem.com/Ajax/UniversalSelectorFiltersPopin?facet={806E2FFA-2F53-49AB-A9C8-600CD7E573EF}&val=&count=&url=https%3a%2f%2fpolymer-additives.specialchem.com%2fselectors&actualQuery=KChfbGFuZ3VhZ2U6KGVuKSBBTkQgKF9wYXRoOihkYTUwMTk5ODQzMzI0NjkyODcyNGZjYWYzYjBlYzM5YSkgT1IgX3BhdGg6KGRhNTAxOTk4NDMzMjQ2OTI4NzI0ZmNhZjNiMGVjMzlhKSkpIEFORCBfdGVtcGxhdGU6KGRhYzU3ODljOWMwYjQxY2FiNWQxZGUxMDY3MjFjMTQ0KSk=&extraQuery=&cmpwith=&tgtitem=']

    def parse(self, response):
        data = {}
    
        a = []
        for products in response.css('.items-list li'):

            product_attr = {}
            
            if((products.css('a .name::text').get()).replace("\n", "") != " "):
                product_attr['application'] = (products.css('a .name::text').get()).replace("\n", "")
            else:
                product_attr['application'] = (products.css('a .vam .col::text').get()).replace("\n", "")
            
            product_attr['url'] = products.css('a::attr(href)').get()

            if('Ajax' not in products.css('a::attr(href)').get()):

                a.append(product_attr)
    
                    
        data['applications'] = a

        yield(data)