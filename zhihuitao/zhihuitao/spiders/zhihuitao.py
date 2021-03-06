#coding=utf-8
from zhihuitao.items import ZhihuitaoItem
import logging
import scrapy
class ZhihuitaoSpider(scrapy.Spider):
    name="zhihuitao"
    start_urls = [
       "http://zhihuitao.cn/Demand/lists?p=1",
    ] 
    def parse(self,response):
        self.num=1
        self.url="http://zhihuitao.cn/Demand/lists?p="+str(self.num)
        logging.log(logging.INFO, "==start==")
        infos=response.xpath("//div/div/ul/li[@class='demandList']")
        item=ZhihuitaoItem()
        for info in infos:
        	item['title']=info.xpath('div[1]/div[2]/a/text()').extract()
        	item['url']=info.xpath('div[1]/div[2]/a/@href').extract()
        	item['content']=info.xpath('div[1]/div[2]/div/text()').extract()
        	yield item
        self.num=self.num+1
        if self.num <= 61:
            request=scrapy.Request(url=self.url)
            yield request
            
