# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class XmlycrawlItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    play_path_32 = scrapy.Field()
    title = scrapy.Field()
    category_name = scrapy.Field()
    duration = scrapy.Field()
    nickname = scrapy.Field()
    play_count = scrapy.Field()
    cover_url_142 = scrapy.Field()
    comments_count = scrapy.Field()
    intro = scrapy.Field()
    time_until_now = scrapy.Field()
    formatted_created_at = scrapy.Field()
    category_title = scrapy.Field()
    play_path_64 = scrapy.Field()
    shares_count = scrapy.Field()
    album_title = scrapy.Field()
    is_free = scrapy.Field()
    id = scrapy.Field()
    favorites_count = scrapy.Field()
    upload_id = scrapy.Field()
    uid = scrapy.Field()
    have_more_intro = scrapy.Field()
    is_paid = scrapy.Field()
    discounted_price = scrapy.Field()
    is_favorited = scrapy.Field()
    play_path = scrapy.Field()
    played_secs = scrapy.Field()
    cover_url = scrapy.Field()
    waveform = scrapy.Field()
    price = scrapy.Field()
    album_id = scrapy.Field()
    file_urls= scrapy.Field()
    files = scrapy.Field()
    pass
