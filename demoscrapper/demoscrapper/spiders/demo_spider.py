import scrapy
from w3lib import html
class DemoSpider(scrapy.Spider):
    name = "demospider"
    start_urls = [
        "https://www.tc.columbia.edu/counseling-and-clinical-psychology/clinical/degrees--requirements/clinical-psychology-phd/",
    ]

    def parse(self, response):
        for content in response.css("div.inner-content p"):
            yield {
                "text": html.remove_tags(content.get())
            }