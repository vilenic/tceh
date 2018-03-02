import scrapy

# Команда запуска из консоли:
# scrapy crawl habrahabr_posts -o posts.json

class habrSpider(scrapy.Spider):
    name = "habrahabr_posts"
#    allowed_domains = 'www.habrahabr.ru/'
    start_urls = ['https://habrahabr.ru/users/zhovner/posts/']

    def parse(self, response):

        post_pages = response.css('div.posts_list h2 a.post__title_link::attr(href)').extract()
        for i in range(len(post_pages)):
            next_page = post_pages[i]
            if next_page:
                yield response.follow(next_page, self.parsePost)

        next_author_page = response.css('div.page__footer a.arrows-pagination__item-link_next::attr(href)').extract_first()
        if next_author_page:
            yield response.follow(next_author_page, self.parse)

    def parsePost(self, response):

        title = response.css('div.post__wrapper h1.post__title_full span.post__title-text::text').extract_first()

        post_text_raw = response.css('div.js-mediator-article p::text').extract()
        post_text_formatted = []

        if not post_text_raw:
            post_text_raw = response.css('div.js-mediator-article::text').extract()

        for i in range(len(post_text_raw)):
            post_text_raw[i] = post_text_raw[i].strip()
            if post_text_raw[i]:
                post_text_formatted.append(post_text_raw[i])

        yield {

                'title' : title,
                'text' : post_text_formatted,

                }

