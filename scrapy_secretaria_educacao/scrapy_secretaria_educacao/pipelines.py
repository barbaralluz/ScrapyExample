# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html

import pymongo

from scrapy.conf import settings
from scrapy.exceptions import DropItem
from scrapy import log

class ScrapySecretariaEducacaoPipeline(object):
    def __init__(self):
        connection = pymongo.MongoClient("mongodb://mongodb:rNOseeTqbmHdEoYI@testcluster-shard-00-00-8rahr.mongodb.net:27017,testcluster-shard-00-01-8rahr.mongodb.net:27017,testcluster-shard-00-02-8rahr.mongodb.net:27017/test?ssl=true&replicaSet=TestCluster-shard-0&authSource=admin&retryWrites=true"
        )
        db = connection[settings['MONGODB_DB']]
        self.collection = db[settings['MONGODB_COLLECTION']]

    def process_item(self, item, spider):
        valid = True

        for data in item:
            if not data:
                valid = False
                raise DropItem("Dados incorretos, ausência de {0}!".format(data))
        if valid:
            self.collection.insert(dict(item))
            log.msg("Notícia inserida no BD!",
                    level=log.DEBUG, spider=spider)
        return item
