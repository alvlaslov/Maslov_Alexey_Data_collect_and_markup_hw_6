import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from scrapy.loader import ItemLoader
from ..items import UnsplashItem
from itemloaders.processors import MapCompose

class UnsplashImgsSpider(CrawlSpider):
    name = "unsplash_imgs"
    allowed_domains = ["unsplash.com"]
    start_urls = ["https://unsplash.com/images/things/money"]

    rules = (
        Rule(LinkExtractor(restrict_xpaths=('//div[@class="GFY23"]/div/a')), callback='parse_item', follow=True),
        
    )


    def parse_item(self, response):
        loader = ItemLoader(item=UnsplashItem(), response=response)
        loader.default_imput_processor = MapCompose(str.strip)

        name_img = response.xpath('//h1/text()').get()
        if name_img:
            loader.add_xpath('name', '//h1/text()')
        else:
            loader.add_value('name', 'None')

        category_img = response.xpath('//div[@class="nzfdq"]/a[@class="glD4s eziW_ HaWw1"]/text()').get()
        if category_img:
            loader.add_xpath('category', '//div[@class="nzfdq"]/a[@class="glD4s eziW_ HaWw1"]/text()')
        else:
            loader.add_value('category', 'None')

        url_img = response.xpath('//div[@class="MorZF"]/img@src').get()
        loader.add_value('image_urls', url_img) 

        

        # loader.add_value('image_urls', absolute_umage_urls)


        yield loader.load_item()

 