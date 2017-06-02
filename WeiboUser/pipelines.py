# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
from WeiboUser.spiders.sql import Sql
from WeiboUser.items import WeibouserItem

class WeibouserPipeline(object):
    def process_item(self, item, spider):

        screen_name = item['screen_name']
        verified_reason = item['verified_reason']
        follow_count = item['follow_count']
        followers_count = item['followers_count']

        print("Start storing")

        Sql.create_database()
        Sql.create_tables()
        Sql.insert_dd_name(screen_name,verified_reason,follow_count,followers_count)

        # return item
