import scrapy
from ..spider_utils import gen_keywords

class ArchivesSpider(scrapy.Spider):
    def __init__(self, name=None, **kwargs):
        self.start_urls = ['https://asb.nadir.org/tp1.php?urlpara=1000']
        self.start_urls.extend(['https://asb.nadir.org/tp1.php?urlpara=%d' % i for i in range(1001, 1000000)])
        super(ArchivesSpider, self).__init__(name, **kwargs)

    name = 'archives_spider'
    allowed_domains = ['asb.nadir.org']
    start_urls = ['https://asb.nadir.org/tp1.php?urlpara=1000']
    current_url = 'https://asb.nadir.org/tp1.php?urlpara=1000'


    def parse(self, response):



        keywords = gen_keywords('keywords.txt')
        
        for keyword in keywords:
            relevantContent = []

            #build string
            xpathStr = "//*[contains(text(), '"
            xpathStr += keyword
            xpathStr += "')]"

            #take this page and grep all instances
            relevantContent = response.xpath(xpathStr).getall()
            #if there is relevant content then get all the other info too
            if(relevantContent):
                title = response.xpath('//*[@id="content"]/h2[1]/text()').get()
                subtitle = response.xpath('//*[@id="tp1"]/tr[1]/td[2]/span/text()').get()
            

            #send each response off to the output file
            for item in relevantContent:
                yield{
                    "url" : response.request.url,
                    "Title of article" : title,
                    "Subtitle" : subtitle,
                    "Keywords triggered" : keyword,
                    "Tag" : strCleanup(item)
                }

def strCleanup(string):
    retVal = ""
    inTag = False
    for char in string:
        if char == '<':
            inTag = True
            continue
        elif char == '>':
            inTag = False
            continue
        elif inTag:
            continue
        else:
            retVal += char
    return retVal