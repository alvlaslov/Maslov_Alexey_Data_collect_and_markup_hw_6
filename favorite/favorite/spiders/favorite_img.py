import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from scrapy.loader import ItemLoader
from ..items import FavoriteItem
from itemloaders.processors import MapCompose
from urllib.parse import urljoin



class FavoriteImgSpider(CrawlSpider):
    name = "favorite_img"
    allowed_domains = ["favorit-motors.ru"]
    start_urls = ["https://favorit-motors.ru/catalog/stock/"]

    rules = (Rule(LinkExtractor(restrict_xpaths=("//div[@class='b_car_list__body']/a")), callback="parse_item", follow=True),)

    def parse_item(self, response):
        loader = ItemLoader(item=FavoriteItem(), response=response)
        loader.default_input_processor = MapCompose(str.strip)

        loader.add_xpath('name', '//h1/text()')

        js_old_price = response.xpath('//div[@class="b_detail_info__price_old js_old_price"]/text()').get()

        if js_old_price:
            loader.add_value('price', js_old_price)
        else:
            loader.add_xpath('price', '//div[@class="b_detail_info__price js_discount_price/text()')


        relative_image_urls = response.xpath('//div[@class="b_detail_gallery__img"]/a/@href').getall()
        absolute_image_urls = [urljoin("https://favorit-motors.ru", img_url)for img_url in relative_image_urls] 
        loader.add_value('image_urls', absolute_image_urls)

        yield loader.load_item()







