#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals
import os


AUTHOR = u'nullne'
SITENAME = u'NULLNE'
SITEURL = ''
#GITHUB_URL = 'https://github.com/nullne'
GOOGLE_ANALYTICS = "UA-56583262-1"

THEME = 'themes/yaner'
PLUGIN_PATHS = ["plugins"]
PLUGINS = ['tipue_search', 'encrypt_content', 'photos', 'liquid_tags.vimeo', 'pelican_gist']
ENCRYPT_CONTENT = {
    'title_prefix': '<i class="lock icon"></i>',
    'summary': 'This content is encrypted.',
    'categories': [u'Dear Diary'],
    'password': 'love'
}
DIRECT_TEMPLATES = (('index', 'tags', 'categories', 'authors', 'archives', 'search'))

PATH = 'content'
STATIC_PATHS = ['million', 'archive', 'background']
#ARTICLE_PATHS = ['blog']
ARTICLE_SAVE_AS = '{category}/{date:%Y}/{slug}.html'
ARTICLE_URL = '{category}/{date:%Y}/{slug}.html'
PAGE_SAVE_AS = '{slug}.html'
PAGE_URL = '{slug}.html'
DRAFT_SAVE_AS = 'draft/{slug}.html'
DRAFT_URL = 'draft/{slug}.html'

# photos
PHOTO_LIBRARY =  os.path.join(
    os.path.dirname(os.path.abspath(__file__)),
    'content/images/')
PHOTO_GALLERY = (144000, 90000, 100)
PHOTO_ARTICLE = (1440, 700, 100)
PHOTO_THUMB = (150, 150, 80)
PHOTO_WATERMARK = True
PHOTO_WATERMARK_TEXT = '@nullne'

SUMMARY_MAX_LENGTH = 10
TIMEZONE = 'Asia/Shanghai'

DEFAULT_LANG = u'en'
DEFAULT_DATE = 'fs'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = 'all-atom.xml'
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None

# Blogroll
LINKS = (('Zonca', 'http://zonca.github.io/'),
        ('Moparx', 'http://moparx.com/'),
        ('Friparia', 'http://blog.friparia.com/'),
        )

# Social widget
SOCIAL = (('GitHub', 'https://github.com/nullne'),
        ('LinkedIn', 'https://www.linkedin.com/pub/le-yu/89/980/1a5'),
        ('豆瓣', 'http://www.douban.com/people/nullnes/'),
        ('微博', 'http://weibo.com/nullne'),)

DEFAULT_PAGINATION = 30

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True

DISPLAY_PAGES_ON_MENU = True
USE_FOLDER_AS_CATEGORY = True
DISPLAY_CATEGORIES_ON_MENU = True

#ARTICLE_ORDER_BY = 'date'
#PAGE_ORDER_BY = 'date'
REVERSE_CATEGORY_ORDER = True
NEWEST_FIRST_ARCHIVES = True
ARTICLE_EXCLUDES = ['archive']
PYGMENTS_RST_OPTIONS = {'classprefix': 'pgcss', 'linenos': 'table'}

CATEGORY_INFO = {
    u'琐碎': u'琐碎的事情',
    u'Hand of Midas': u'点金手，助我点石成金',
    u'Dear Diary': u'记录岁月流逝',
}
