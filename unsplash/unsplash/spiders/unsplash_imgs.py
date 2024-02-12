import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from scrapy.loader import ItemLoader
from ..items import UnsplashItem
from itemloaders.processors import MapCompose

class UnsplashImgsSpider(CrawlSpider):
    name = "unsplash_imgs"
    allowed_domains = ["www.unsplash.com"]
    start_urls = ["https://unsplash.com/images/things/money"]

    rules = (
        Rule(LinkExtractor(restrict_xpaths=('//div[@class="GFY23"]/div/a')), callback='parse_item', follow=True),

    )

    # //figure[@itemprop="image"]/div[@class="GFY23"]/div/a

    def parse_item(self, response):
        print(response.url)
        # loader = ItemLoader(item=UnsplashItem(), response=response)
        # loader.default_imput_processor = MapCompose(str.strip)

        # loader.add_xpath('name', '//h1/text()')
        # views_span = response.xpath('//div[@class="_NeDM"][0]/span/text()').get()
        # loader.add_value('views', views_span)
        # downloads_span = response.xpath('//div[@class="_NeDM"][1]/span/text()').get()
        # loader.add_value('downloads', downloads_span)

 