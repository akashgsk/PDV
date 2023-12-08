# ecommerce/spiders/ecomm.py
import scrapy
#from ecommerce.items import EcommerceItem

class EcommSpider(scrapy.Spider):
    name = "ecommerce"
    start_urls = ['https://getmybooks.com/']

    def parse(self, response):
        # div=response.css(".#slick-slide10 .p-0")
        title = response.css('.secondary-font a::text').extract()
        author = response.css('a.text-gray-700::text').extract()
        #print(author)
        price = response.css('.amount::text').extract()
        #print(price)
        for i in range(len(title)):
            yield {"title": title[i], "author": author[i],"price": price[i].split('\r\n')[0]}
