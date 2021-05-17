import scrapy


class QuotesSpider(scrapy.Spider):
    name = "quotes_spider"
    # spider name could be any name of our choice

    def start_requests(self):
        # helps to perform get requests from website
        urls = ['http://quotes.toscrape.com/page/1/',
                'http://quotes.toscrape.com/page/2/'
                ]
        # we'll then make a generator funtion
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)
            # the above makes a request to the url and when the response
            # comes we'll parse it

    def parse(self, response):
        # this method knows what to do with a particular response
        # to find out which url we made a get request on:
        page_no = response.url.split("/")[-2]
        # to find out the page number,we use the split method,which will
        # return a list and doing [-2] will provide us the page no

        # to save the response in a HTML file,locally:
        filename = "quotes-%s.html" % page_no
        # the above will create the files:
        # quotes-1.html,quotes-2.html and so on

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
        # with open(filename, 'wb') as f:
        #    f.write(response.body)
        #self.log('Saved file %s' % filename)
