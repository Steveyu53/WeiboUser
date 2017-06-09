# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class WeibouserItem(scrapy.Item):
    # define the fields for your item here like:
    screen_name = scrapy.Field()

    verified_reason = scrapy.Field()

    follow_count = scrapy.Field()

    followers_count = scrapy.Field()

    # h_ip = scrapy.Field()

    pass
