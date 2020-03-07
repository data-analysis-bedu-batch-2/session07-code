import scrapy

class QuoteSpider(scrapy.Spider):

    name = "quotes"

    start_urls = [
        "http://quotes.toscrape.com/"
    ]

    def parse(self, response):
        quotes = response.css('div.quote')

        for quote in quotes:
            yield {
                "quote": quote.css('span.text::text').get(),
                "author": quote.css('small.author::text').get()
            } 

        li_next = response.css('li.next')
        href = li_next.css("a::attr('href')").get()
        if li_next and href:
            yield response.follow(href, self.parse)




