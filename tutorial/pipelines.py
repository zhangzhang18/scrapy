# -*- coding: utf-8 -*-
# 　pipelines.py：用来将提取出来的Item进行处理，处理过程按自己需要进行定义
# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html

from scrapy import signals
import json
import codecs
import sys
import json
import codecs

reload(sys)
sys.setdefaultencoding("utf-8")


class SinaPipeline(object):
    def process_item(self, item, spider):
        link_url = item['link_url']
        file_name = link_url[7:-6].replace('/', '_')
        file_name += ".txt"
        fp = open(item['path'] + '/' + file_name, 'w')
        fp.write(item['content'])
        fp.close()
        return item


class W3SchoolPipeline(object):
    def __init__(self):
        self.file = codecs.open('w3school_data_utf8.json', 'wb', encoding='utf-8')

    def process_item(self, item, spider):
        line = json.dumps(dict(item)) + '\n'
        # print line
        self.file.write(line.decode("unicode_escape"))
        return item


class TutorialPipeline(object):
    def process_item(self, item, spider):
        return item
