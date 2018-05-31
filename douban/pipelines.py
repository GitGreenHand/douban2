# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import scrapy
import  json
from scrapy.pipelines.images import ImagesPipeline

'''
class DoubanPipeline(object):
    def __init__(self):
        self.f=open("douban.json",'w')

    def process_item(self, item, spider):
        content=json.dumps(dict(item),ensure_ascii=False)+',\n'
        self.f.write(content.encode('utf-8'))
        return item

    def spider_close(self):
        self.f.close()

'''
class DoubanPipeline(ImagesPipeline):
    def get_media_requests(self, item, info):
        image=item['image']
        #print('pipeline_image',image)
        #print("*"*40)
        yield scrapy.Request(image)



