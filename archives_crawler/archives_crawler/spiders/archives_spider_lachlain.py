import scrapy
from spider_utils import gen_keywords


class ArchivesSpiderLachlainSpider(scrapy.Spider):
    name = 'archives_spider_lachlain'
    allowed_domains = ['asb.nadir.org']
    start_urls = ['https://asb.nadir.org/tp1.php?urlpara=1000']
    current_url = 'https://asb.nadir.org/tp1.php?urlpara=1000'

    def parse(self, response):

        keywords = self.gen_keywords('keywords.txt')
        
        for keyword in keywords:

            relevantContent = response.xpath("//*[contains(text(), 'MY TEXT')]").getall()
            for item in relevantContent:
                yield{

                    "url" : self.current_url,
                    "Keywords triggered" : item.extract()

                }




