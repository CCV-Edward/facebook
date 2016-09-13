# -*- coding: utf-8 -*-

# Scrapy settings for mss project
#
# For simplicity, this file contains only the most important settings by
# default. All the other settings are documented here:
#
#     http://doc.scrapy.org/en/latest/topics/settings.html
#

BOT_NAME = 'mss'

SPIDER_MODULES = ['mss.spiders']
NEWSPIDER_MODULE = 'mss.spiders'

# Crawl responsibly by identifying yourself (and your website) on the user-agent
USER_AGENT = "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:34.0) Gecko/20100101 Firefox/34.0"
PROXIES = [
  {'ip_port': '127.0.0.1:8118', 'user_pass': ''},
]

DOWNLOADER_MIDDLEWARES = {
    'mss.middlewares.ProxyMiddleware': 543,
    'mss.middlewares.PrintUrlMiddleware': 543,
}

ITEM_PIPELINES = {
   'mss.pipelines.JSONPipeline': 300,
}