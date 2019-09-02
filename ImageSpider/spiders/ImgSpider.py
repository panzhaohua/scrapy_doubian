# @Time    : 2019/1/7 15:25
# @Author  : MosesPan
# @Email   : 269258169@qq.com
# @File    : ImgSpider.py
# @Software: PyCharm

import scrapy
from  ImageSpider.items import ImagespiderItem

class ImgSpider(scrapy.Spider):
    name = 'ImgSpider'
    allowed_domains = ['douban.com']
    start_urls = ['https://www.douban.com/doulist/13704241/']

    def parse(self, response):
        item = ImagespiderItem() #实例化item
        # imgurls = response.css(".index img::attr(src)").extract() #注意这里是一个集合也就是多张图片
        imgurls = response.xpath('//div[@class="post"]/a/img/@src').extract()
        item['imgurl'] = imgurls
        yield item