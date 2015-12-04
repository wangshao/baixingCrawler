# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class baixingItem(scrapy.Item):
    # define the fields for your wo tem here like:
    # name = scrapy.Field()
    title 	= scrapy.Field()
    url   	= scrapy.Field()
    name 	= scrapy.Field()
    phone 	= scrapy.Field()
    price 	= scrapy.Field()
    desc	= scrapy.Field()
    date 	= scrapy.Field()
