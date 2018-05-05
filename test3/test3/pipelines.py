# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
from test3.items import ImforItem
from test3.items import MyImageItem



class TitleAndPricePipeline(object):
    def process_item(self, item, spider):
        if isinstance(item, ImforItem):
            file = open("PriceAndTitle.txt", 'a')
            for title, price in zip(item['titles'], item['prices']):
                file.write(title + ' ' + price + '\n')
        return item


class MyImagesPipeline(object):
    def process_item(self, item, spider):
        if isinstance(item, MyImageItem):

        return item
