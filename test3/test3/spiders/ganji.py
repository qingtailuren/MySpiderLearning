# -*- coding: utf-8 -*-
import scrapy
from test3.items import ImforItem
import time


class Myspider(scrapy.Spider):
    name = "haha"
    start_urls = ['http://fz.ganji.com/fang5/']
    num = 0

    def parse(self, response):
        header = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.181 Safari/537.36'}
        urlList = response.xpath("//a[@class = 'next']/@href").extract()
        print(urlList)
        urlList[0] = 'http://fz.ganji.com' + urlList[0]
        titles = response.xpath("//dd[@class = 'dd-item title']/a/text()").extract()
        prices = response.xpath("//span[@class = 'num js-price']/text()").extract()
        imforitem = ImforItem()
        imforitem['titles'] = titles
        imforitem['prices'] = prices
        yield imforitem
        time.sleep(1)
        print(urlList)
        self.num = self.num + 1
        if self.num < 4:
            yield scrapy.Request(url=urlList[0], headers=header, callback=self.parse)
