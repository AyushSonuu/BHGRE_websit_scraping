import scrapy
from scrapy.crawler import CrawlerProcess
from scrapy.utils.project import get_project_settings
from BHGRE.spiders.agent_details import AgentDetailsSpider

process =CrawlerProcess()
process.crawl(AgentDetailsSpider)
process.start()
