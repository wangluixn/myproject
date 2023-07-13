# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
import json
from pymongo import MongoClient


class MycasePipeline:
    def __init__(self):
        self.file = open("itcast.json",'w')

    def process_item(self, item, spider):
        item = dict(item)
        #print(type(item))
        # json_data= json.dumps(item,ensure_ascii=False) + ',\n'
        # self.file.write(json_data)
        return item
    def __del__(self):
        self.file.close()



class MycaseMysql:
    def process_item(self, item, spider):

        #print(item)
        return item

class MangoPipeline(object):
    def open_spider(self,spider):
        self.client = MongoClient('127.0.0.1',27017)
        self.db = self.client['mydb']
        self.col = self.db['itcast']

    def process_item(self, item, spider):
        data = dict(item)
        self.col.insert_one(data)
        return item

    def close_spider(self,spider):
        self.client.close()


