#!/usr/bin/env python


from scrapy.cmdline import execute
import os

# execute(['scrapy', 'genspider', 'main_spider',''])
execute(['scrapy', 'crawl', 'main_spider'])

# execute(['scrapy','genspider','sogou_weixin_wxpublic','sogou.com'])