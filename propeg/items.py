# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class PropegItem(scrapy.Item):
    # define the fields for your item here like:
    propname = scrapy.Field()
    propname = scrapy.Field()
    proptype = scrapy.Field()
    address = scrapy.Field() 
    sqm = scrapy.Field() 
    price = scrapy.Field() 
    bed = scrapy.Field() 
    bath = scrapy.Field() 
    link = scrapy.Field()
    ref = scrapy.Field()
    description = scrapy.Field()
    json1 = scrapy.Field()
    json2 = scrapy.Field()


