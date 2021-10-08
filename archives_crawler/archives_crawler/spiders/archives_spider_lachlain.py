import scrapy


class ArchivesSpiderLachlainSpider(scrapy.Spider):
    name = 'archives_spider_lachlain'
    allowed_domains = ['https://asb.nadir.org/archivsystematik.php']
    start_urls = ['http://https://asb.nadir.org/archivsystematik.php/']

    def parse(self, response):
        pass
