# -*- coding: utf-8 -*-

# 　items.py：用来定义需要保存的变量，其中的变量用Field来定义，有点像python的字典
import scrapy
from scrapy.item import Item, Field


class TutorialItem(Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    parent_title = Field()
    parent_url = Field()

    second_title = Field()
    second_url = Field()
    path = Field()

    link_title = Field()
    link_url = Field()
    head = Field()
    content = Field()
    pass


class W3schoolItem(Item):
    title = Field()
    link = Field()
    desc = Field()


class Website(Item):
    headTitle = Field()
    description = Field()
    url = Field()


class DmozItem(Item):
    title = Field()
    link = Field()
    desc = Field()

