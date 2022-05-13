import scrapy

class BooksSpider(scrapy.Spider):
    # name of the spider. Must be unique.
    name = "books"
    start_urls = [
        "https://books.toscrape.com"
    ]

    # has a response object that contains HTML information about our request and whether
    # it succeeded, etc.
    def parse(self, response):
        titles = response.css("article.product_pod h3 a::attr(title)").getall()
        prices = response.css("p.price_color::text").getall()
        
        for title, price in zip(titles, prices):
            yield {
                "title": title,
                "price": price
            }

            next_page = response.css("li.next a::attr(href)").get()
            
            # if there is a next page, if it exists, if Scrapy found the next button
            if next_page is not None:    
                # gets full url including starting url + specifications of next_page
                next_page_url = response.urljoin(next_page)
                # scrape the next page by sending a request with the next_page_url
                # that calls the parse function (recursion!)
                yield scrapy.Request(url = next_page_url, callback = self.parse)

        # alternate solution
        # since both title and price are nested under the same parent article
        # for entry in response.css("article.product_pod"):
        #     title = entry.css("h3 a::attr(title)").get()
        #     price = entry.css("p.price_color::text").get()

        #     yield {
        #         "title": title, 
        #         "price": price
        #     }

