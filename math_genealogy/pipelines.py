# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
import pymongo
from scrapy.exceptions import DropItem

class MathGenealogyPipeline(object):



    def __init__(self):
        conn = pymongo.MongoClient("172.18.79.31:27017")
        db = conn['mathdb']
        self.coll = db['person']
        self.crawled = set()
        cur = self.coll.find()
        for doc in cur:
            self.crawled.add(doc['fingerprint'])

        print("%d crawled items loaded" % len(self.crawled))


    def process_item(self, item, spider):

        if item['fingerprint'] in self.crawled:
            DropItem("crawled %s" % item['name'])

        self.coll.insert(dict(item))
        self.crawled.add(item['fingerprint'])

        return item
