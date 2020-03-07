import scrapy
import time
from selenium import webdriver


class SegundaManoSpider(scrapy.Spider):

    name = "segunda_mano"

    start_urls = [
        "https://www.segundamano.mx/inmuebles"
    ]

    def __init__(self):
        self.webdriver = webdriver.Chrome()

    def parse(self, unloaded_page):
        self.webdriver.get(unloaded_page.url)
        time.sleep(5)
        response = scrapy.Selector(text=self.webdriver.page_source)

        propiedades = response.css('div.AdCard__StyledInfoContainer-s2jc2d-12')

        for propiedad in propiedades:
            yield {
                "name": propiedad.css('div.AdCard__StyledText-s2jc2d-13::text').extract(),
                "price": propiedad.css('div.AdCard__StyledPrice-s2jc2d-8::text').extract(),
            }