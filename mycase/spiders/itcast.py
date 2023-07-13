import scrapy
from ..items import MycaseItem
from redis import Redis


class ItcastSpider(scrapy.Spider):
    name = "itcast"
    allowed_domains = ["itcast.cn"]
    start_urls = ["https://www.itcast.cn/channel/teacher.shtml"]

    def parse(self, response):
        #print(response)
        #print(response.text)
        node_list = response.xpath("//div[@class='li_txt']")
        for teacher in node_list:
            item = MycaseItem()
            name = teacher.xpath('./h3/text()').extract_first().strip()   # xpath返回的都是列表，元素根据匹配规则来(e.g. text())
            title = teacher.xpath('./h4/text()').extract_first().strip()
            info = teacher.xpath('./p/text()').extract_first().strip()
            item['name'] = name
            item['title'] = title
            item['info'] = info
            
            yield item

