# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
# ecommerce/pipelines.py
from itemadapter import ItemAdapter
import sqlite3

class EcommercePipeline:

    def __init__(self):
        self.create_connection()
        self.create_table()

    def create_connection(self):
        self.conn = sqlite3.connect("mybook_db")
        self.curr = self.conn.cursor()

    def create_table(self):
        self.curr.execute(""" DROP TABLE IF EXISTS mybook """)   
        self.curr.execute(""" Create Table mybook (
                            title text,
                            author text,
                            price text
                            )""")

    def process_item(self, item, spider):
        self.store_db(item)
        return item

    def store_db(self, item):
        # title = str(item['title']) if item['title'] is not None else None
        # author = str(item['author']) if item['author'] is not None else None
        # price = str(item['price']) if item['price'] is not None else None
        self.curr.execute("""INSERT INTO mybook (title, author, price) VALUES (?, ?, ?)""",
                            (
                                item['title'],
                                item['author'],
                                item['price'] 
                                ))

        self.conn.commit()
