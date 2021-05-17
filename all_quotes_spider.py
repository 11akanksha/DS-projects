import scrapy


class QuotesSpider(scrapy.Spider):
    name = "quotes_spider"
    # spider name could be any name of our choice

    def start_requests(self):
        # helps to perform get requests from website
        urls = ['http://quotes.toscrape.com/page/1/'
                ]
        # we'll then make a generator funtion
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)
            # the above makes a request to the url and when the response
            # comes we'll parse it

    def parse(self, response):
        # this method knows what to do with a particular response

        # to convert the file in a json format:
        for q in response.css("div.quote"):
            text = q.css("span.text::text").get()
            author = q.css("small.author::text").get()
            tags = q.css("a.tag::text").getall()
        # we'll now yeild this in the form of a dictionary:
            yield{
                'text': text,
                'author': author,
                'tags': tags
            }

        # till now we got the parsed response from the first page
        # now we'll try to automate the spider so that it automatically
        # crawls and extracts all the quotes from the website.
        # so ...if next page exists:
        next_page = response.css('li.next a::attr(href)').get()
        if next_page is not None:
            next_page = response.urljoin(next_page)
            yield scrapy.Request(next_page, callback=self.parse)
