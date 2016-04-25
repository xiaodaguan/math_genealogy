# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class MathGenealogyItem(scrapy.Item):
    # define the fields for your item here like:
    id = scrapy.Field()
    name = scrapy.Field()
    school = scrapy.Field()
    year = scrapy.Field()
    descendants = scrapy.Field()  # count
    parent_id = scrapy.Field()

    # common fields
    url = scrapy.Field()  # page url
    fingerprint = scrapy.Field()
