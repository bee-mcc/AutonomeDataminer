import scrapy
from ..spider_utils import gen_keywords

class ArchivesSpiderLachlainSpider(scrapy.Spider):
    def __init__(self, name=None, **kwargs):
        self.start_urls = ['https://asb.nadir.org/tp1.php?urlpara=1000']
        self.start_urls.extend(['https://asb.nadir.org/tp1.php?urlpara=%d' % i for i in range(1001, 1000000)])
        super(ArchivesSpiderLachlainSpider, self).__init__(name, **kwargs)

    name = 'archives_spider_lachlain'
    allowed_domains = ['asb.nadir.org']
    start_urls = ['https://asb.nadir.org/tp1.php?urlpara=1000']
    current_url = 'https://asb.nadir.org/tp1.php?urlpara=1000'


    def parse(self, response):

        keywords = gen_keywords('keywords.txt')
        
        for keyword in keywords:
            #build string
            xpathStr = "//*[contains(text(), '"
            xpathStr += keyword
            xpathStr += "')]"

            #take this page and grep all instances
            relevantContent = response.xpath(xpathStr).getall()
            
            #send each response off to the output file
            for item in relevantContent:
                yield{
                    "url" : self.current_url,
                    "Keywords triggered" : keyword,
                    "Tag" : item
                }




