# -*- coding: utf-8 -*-
import hashlib

import re
import scrapy

from math_genealogy.items import MathGenealogyItem


class MainSpiderSpider(scrapy.Spider):
    name = "main_spider"
    allowed_domains = ["nodak.edu"]
    start_urls = (
        'https://www.genealogy.math.ndsu.nodak.edu/id.php?id=134975',
    )

    def parse(self, response):
        '''
        每一页都是一样,解析完child_url,然后请求递归调用自身作为callback即可
        :param response:
        :return:
        '''

        tr_stus = response.xpath("//tr/td[1]")
        next_urls = []
        if len(tr_stus) > 0:
            for i in range(2, len(tr_stus) + 2):
                item = MathGenealogyItem()

                item['name'] = response.xpath("//tr[%d]/td[1]/a/text()" % i).extract()
                item['url'] = "https://www.genealogy.math.ndsu.nodak.edu/%s" % response.xpath("//tr[%d]/td[1]/a/@href" % i).extract()[0].encode('utf-8')
                item['school'] = response.xpath("//tr[%d]/td[2]/text()" % i).extract()
                item['year'] = response.xpath("//tr[%d]/td[3]/text()" % i).extract()[0] if len(response.xpath("//tr[%d]/td[3]/text()" % i).extract()) > 0 else None
                item['descendants'] = int(response.xpath("//tr[%d]/td[4]/text()" % i).extract()[0]) if len(response.xpath("//tr[%d]/td[4]/text()" % i).extract()) > 0 else None

                next_urls.append(item['url'])
                item['fingerprint'] = hashlib.md5(item['url']).hexdigest()
                item['parent_id'] = int(re.search("id=\d+", response.url).group(0).replace("id=", ""))
                item['id'] = int(re.search("id=\d+",item['url']).group(0).replace("id=",""))

                yield item

        for url in next_urls:
            yield scrapy.Request(url)
