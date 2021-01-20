import scrapy
from movie_review.items import MovieReviewItem
from scrapy.http import Request

URL = 'http://movie.naver.com/movie/point/af/list.nhn?&page=%s'
start_page = 1

# content -> 40개 데이터(공백포함) -> 10개 데이터 (공백 제거)
def remove_space(contents:list) -> list:
    result = []
    # 공백 제거
    for i in range(len(contents)):
        if len(contents[i].strip()) > 0:
            result.append(contents[i].strip())
    return result


class MybotSpider(scrapy.Spider):
    name = 'mybot'
    allowed_domains = ['naver.com']
    start_urls = [URL % start_page]
    
    # 페이징 하여 3 페이지 까지 출력
    def start_requests(self):
        for i in range(3):  # 1~3 페이지 
            yield Request(url = URL % (i + start_page), callback=self.parse)


    def parse(self, response):
        titles = response.xpath(
            '//*[@id="old_content"]/table/tbody/tr/td[2]/a[1]/text()').extract()
        scores = response.xpath(
            '//*[@id="old_content"]/table/tbody/tr/td[2]/div/em/text()').extract()
        contents = response.xpath(
            '//*[@id="old_content"]/table/tbody/tr/td[2]/text()').extract()
        converted_contents = remove_space(contents)
        authors = response.css('.author::text').extract()
        dates = response.xpath(
            '//*[@id="old_content"]/table/tbody/tr/td[3]/text()').extract()

        for row in zip(titles, scores, converted_contents, authors, dates):
            item = MovieReviewItem()
            item['title'] = row[0]
            item['score'] = row[1]
            item['content'] = row[2]
            item['author'] = row[3]
            item['date'] = row[4]

            yield item

            

        # items = []
        # for idx in range(len(titles)):
        #     item = MovieReviewItem()
        #     item['title'] = titles[idx]
        #     item['score'] = scores[idx]
        #     item['content'] = converted_contents[idx]
        #     item['author'] = authors[idx]
        #     item['date'] = dates[idx]

        #     items.append(item)

        # return items
