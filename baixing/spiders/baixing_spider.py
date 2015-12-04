# -*- coding: utf-8 -*-
from scrapy import Request
from scrapy.spiders import CrawlSpider,Rule
from scrapy.linkextractors import LinkExtractor
from scrapy.selector import Selector
from scrapy.utils.response import get_base_url
from baixing.items import baixingItem
class BaixingSpider(CrawlSpider):
    name = "baixing"
    allowed_domains = ["baixing.com"]

    def start_requests(self):
    	header = {'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/47.0.2526.73 Safari/537.36'}
        yield Request(url="http://shanghai.baixing.com/zhengzu/", headers=header)
        yield Request(url="http://beijing.baixing.com/zhengzu/",  headers=header)
        yield Request(url="http://guangzhou.baixing.com/zhengzu/",  headers=header)
        yield Request(url="http://shenzhen.baixing.com/zhengzu/",  headers=header)
        yield Request(url="http://suzhou.baixing.com/zhengzu/",  headers=header)
        yield Request(url="http://shenyang.baixing.com/zhengzu/",  headers=header)
        yield Request(url="http://shijiazhuang.baixing.com/zhengzu/",  headers=header) 
        yield Request(url="http://hangzhou.baixing.com/zhengzu/",  headers=header)
        yield Request(url="http://dalian.baixing.com/zhengzu/",  headers=header)
        yield Request(url="http://xian.baixing.com/zhengzu/",  headers=header)
        yield Request(url="http://zhengzhou.baixing.com/zhengzu/",  headers=header)
        yield Request(url="http://chengdu.baixing.com/zhengzu/",  headers=header)
        yield Request(url="http://tianjin.baixing.com/zhengzu/",  headers=header)
        yield Request(url="http://qingdao.baixing.com/zhengzu/",  headers=header)
        yield Request(url="http://wuhan.baixing.com/zhengzu/",  headers=header)
        yield Request(url="http://jinan.baixing.com/zhengzu/",  headers=header)
        yield Request(url="http://nanjing.baixing.com/zhengzu/",  headers=header)


    rules = (                                                          
    	Rule (LinkExtractor(restrict_xpaths=('//li[@data-aid]/a',))
        , callback='parse_item'
        , process_request='_process_request'),
    	Rule (LinkExtractor(allow=(".*page=[1-5]$"),restrict_xpaths=("//ul[@class='list-pagination']/li[last()]/a",))
        , follow= True
        , process_request='_process_request'),
    )

    def _process_request(self, request):
		request.headers.appendlist('User-Agent',
		'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/47.0.2526.73 Safari/537.36')
		return request

    def parse_item(self, response):
    	item = baixingItem()
    	self.logger.info('Hi, this is parse! ')
        item['title'] = response.xpath("//div[@class='viewad-title ']/h1/text()").extract()
        self.logger.info('Hi, this is an item page! %s', item['title'][0].encode('utf-8'))
        item['url'] = response.url
        item['phone'] = response.xpath("//a[@class='contact-no']/text()").extract()
        item['price'] = response.xpath(u"//span[@class='meta-价格']/text()").extract()
        item['date'] = response.xpath("//div[@class='viewad-actions']/span[1]/text()").extract()
        item['name'] = response.xpath("//a[@class='poster-name']/text()").extract()
        item['desc'] = response.xpath("//div[@class='viewad-text']/text()").extract()
        return item