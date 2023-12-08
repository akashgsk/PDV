import scrapy
from ..items import QuotetutorialItem

class QuoteSpider(scrapy.Spider):

    name='project1'
    start_urls =['https://quotes.toscrape.com/']

    def parse(self,response):
        #1.quotes 2.author 3.tag

        items = QuotetutorialItem() 
        all_div_quotes = response.css('div.quote')

        for project1 in all_div_quotes:

         title=all_div_quotes.css('span.text::text').extract()
         author=all_div_quotes.css('.author::text').extract()
         tag=all_div_quotes.css('.tag::text').extract()

         items['title']=title
         items['author']=author
         items['tag']=tag

         yield items