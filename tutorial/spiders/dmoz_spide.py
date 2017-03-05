# -*- coding: utf-8 -*-
from scrapy.spider import Spider
from scrapy.spider import Spider
from scrapy.selector import Selector
from tutorial.items import DmozItem

class DmozSpider(Spider):
    name = "dmoz"  # name是Scrapy 识别的爬虫名字，一定要唯一。
    allowed_domains = ["dmoz.org"]  # allowed_domains 是域名白名单
    start_urls = [
        "http://www.dmoz.org/Computers/Programming/Languages/Python/Books/",
        "http://www.dmoz.org/Computers/Programming/Languages/Python/Resources/"
    ]  # start_urls 即种子url （如果没有定义其他Rule的话，也就是只抓取这几页）

    def parse(self, response):
        sel = Selector(response)
        sites = sel.xpath('//ul/li')
        items = []
        for site in sites:
            item = DmozItem()
            item['title'] = site.xpath('a/text()').extract()
            item['link'] = site.xpath('a/@href').extract()
            item['desc'] = site.xpath('text()').extract()
            items.append(item)
        return items