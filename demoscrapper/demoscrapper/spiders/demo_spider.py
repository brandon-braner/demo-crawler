import scrapy
from w3lib import html
class DemoSpider(scrapy.Spider):
    name = "demospider"
    start_urls = [
        "https://www.tc.columbia.edu/counseling-and-clinical-psychology/clinical/degrees--requirements/clinical-psychology-phd/",
    ]

    def parse(self, response):
        with open("output.txt", "w+") as file:
            for content in response.css("div.inner-content p"):
                content = html.remove_tags(content.get())
                content = html.replace_escape_chars(content)
                content = html.remove_comments(content)
                content = html.replace_entities(content)

                file.write(content + '\n')

