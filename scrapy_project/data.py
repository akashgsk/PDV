import scrapy

class QuoteSpider(scrapy.Spider):
    name = 'project1'
    start_urls = ['http://quotes.toscrape.com/']

    def parse(self, response):
         title = response.css('title::text').extract()
         yield{'titletest':title}
    