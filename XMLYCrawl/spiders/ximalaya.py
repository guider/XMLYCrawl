# -*- coding: utf-8 -*-
import scrapy
from XMLYCrawl.items import XmlycrawlItem
import requests

headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.84 Safari/537.36',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
    'Connection': 'keep-alive',
    'Cache-Control': 'max-age=0',
    'Upgrade-Insecure-Requests': '1',
    'Proxy-Connection': 'keep-alive',
    'Accept-Encoding': 'gzip, deflate',
    'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8,zh-TW;q=0.7,la;q=0.6',
    'If-None-Match': '"3ce9f2-4a29c-548f423b77900"',
    'If-Modified-Since': 'Mon, 20 Feb 2017 10:58:12 GMT',
    'Cookie': '_xmLog=xm_1514887962743_jbxh6gzby33lps; x_xmly_traffic=utm_source%3A%26utm_medium%3A%26utm_campaign%3A%26utm_content%3A%26utm_term%3A%26utm_from%3A; _ga=GA1.2.309883584.1514887963; trackType=web; Hm_lvt_4a7d8ec50cfd6af753c4f8aee3425070=1514889188; Hm_lpvt_4a7d8ec50cfd6af753c4f8aee3425070=1514914124'
}


class XimalayaSpider(scrapy.Spider):
    name = "ximalaya"
    allowed_domains = ["ximalaya.com"]
    start_urls = [
        'http://www.ximalaya.com/4228109/album/277579/',
        'http://www.ximalaya.com/4228109/album/277579/?page=2',
        'http://www.ximalaya.com/4228109/album/277579/?page=3',
        'http://www.ximalaya.com/4228109/album/277579/?page=4',
        'http://www.ximalaya.com/4228109/album/277579/?page=5'
    ]

    def parse(self, response):
        print(' ------------------------------------------------------')
        for item in response.xpath('//li/div/a/@href').extract():
            id = item.split('/')[-2]
            jsonUrl = 'http://www.ximalaya.com/tracks/' + id + '.json'
            res = requests.get(jsonUrl, headers=headers).json()
            print(res)
            itemObj = XmlycrawlItem()
            for name in res:
                itemObj[name] = res[name]
            itemObj['file_urls'] = [res['cover_url'],res['cover_url_142'],res['play_path']]
            yield itemObj

    # print(response.xpath('//li/div/a/@href').extract())
    # print(response.xpath('//li/div/a/@title').extract())
    # print(response.xpath('//li/div/a/text()').extract())
    print(' ------------------------------------------------------')

    pass
