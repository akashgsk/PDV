# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

# ecommerce/items.py
import scrapy

class EcommerceItem(scrapy.Item):
    title = scrapy.Field()
    author = scrapy.Field()
    price = scrapy.Field()