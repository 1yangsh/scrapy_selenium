import scrapy
from movie_review.items import MovieReviewItem
# from scrapy.http import Request

# URL = 'http://movie.naver.com/movie/point/af/list.nhn&page=%s'
# start_page = 1


class MybotSpider(scrapy.Spider):
    name = 'mybot'
    allowed_domains = ['naver.com']
    start_urls =['http://movie.naver.com/movie/point/af/list.nhn'] # [URL % start_page]

    # def start_requests(self):
    #     for i in range(2):  # 0 ~ 5
    #         yield Request(url = URL & (i + start_page), callback=self.parse)

    def parse(self, response):
        titles = response.xpath(
            '//*[@id="old_content"]/table/tbody/tr/td[2]/a[1]/text()').extract()
        scores = response.xpath(
            '//*[@id="old_content"]/table/tbody/tr/td[2]/div/em/text()').extract()
        contents = response.xpath(
            '//*[@id="old_content"]/table/tbody/tr/td[2]/text()').extract()
        authors = response.css('.author::text').extract()
        dates = response.xpath(
            '//*[@id="old_content"]/table/tbody/tr/td[3]/text()').extract()

        items = []
        for idx in range(len(titles)):
            item = MovieReviewItem()
            item['title'] = titles[idx]
            item['score'] = scores[idx]
            item['content'] = contents[idx].rstrip()
            item['author'] = authors[idx]
            item['date'] = dates[idx]

            items.append(item)

        return items
