import scrapy


class QuotesSpider(scrapy.Spider):
    name = "quotes"

    def start_requests(self) -> scrapy.Request:
        urls = [
            'https://www.citilink.ru/catalog/videokarty/?p=' + str(i) for i in range(6)
        ]
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response, **kwargs) -> dict:
        for quote in response.css('div.ProductCardHorizontal'):
            if ("3060" in quote.css('div.ProductCardHorizontal__header-block'
                                    ' a.ProductCardHorizontal__title::text').get()):
                yield {
                    'name': quote.css('div.ProductCardHorizontal__header-block'
                                      ' a.ProductCardHorizontal__title::text').get()+"\n",
                    'price': "".join(filter(str.isdigit, str(quote.css(
                                                    ' div.ProductCardHorizontal__price-block'
                                                    ' span.ProductCardHorizontal__price_current-price::text').get()))),
                    'rating': ".".join(filter(str.isdigit, (quote.css(
                                                    ' div.ProductCardHorizontal__icons'
                                                    ' span.ProductCardHorizontal__count::text').get(0)))),
                }
