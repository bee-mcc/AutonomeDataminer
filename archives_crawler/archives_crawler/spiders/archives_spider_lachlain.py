import scrapy
#from spider_utils import gen_keywords

class ArchivesSpiderLachlainSpider(scrapy.Spider):
    name = 'archives_spider_lachlain'
    allowed_domains = ['asb.nadir.org']
    start_urls = ['https://asb.nadir.org/tp1.php?urlpara=1000']
    current_url = 'https://asb.nadir.org/tp1.php?urlpara=1000'

    def parse(self, response):

        #keywords = gen_keywords('keywords.txt')
        keywords = ["Hamburg"]
        
        for keyword in keywords:
            xpathStr = "//*[contains(text(), '"
            xpathStr += keyword
            xpathStr += "')]"
            print("LOOK HERE")
            print(xpathStr)
            relevantContent = response.xpath(xpathStr).getall()
            for item in relevantContent:
                yield{
                    "url" : self.current_url,
                    "Keywords triggered" : keyword,
                    "Tag" : item
                }




