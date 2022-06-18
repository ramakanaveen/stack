from scrapy import Spider

from stack.items import InvestmentItem


class InvestmentSpider(Spider):
    name = "investment"
    allowed_domains = ["markets.businessinsider.com"]
    start_urls = [
            "https://markets.businessinsider.com/index/components/s&p_500",
            ]

    def parse(self, response):
        stocks = response.xpath('//table[@class="table table__layout--fixed"]')
        rows = stocks.xpath('./tbody/tr')
        for row in rows:
            item = InvestmentItem()
            item['name'] = row.xpath('./td')[0].css('a::attr(title)').get()
            item['px'] = row.xpath('./td[2]/text()').get().strip()
            item['pct'] = row.xpath('./td[4]/span')[0].css('span::text').get()

            yield item
