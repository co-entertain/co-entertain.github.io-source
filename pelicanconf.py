#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = u'nullne'
SITENAME = u'NULLNE'
SITEURL = ''
#GITHUB_URL = 'https://github.com/nullne'
GOOGLE_ANALYTICS = "UA-56583262-1"

THEME = 'themes/nullne'
PLUGIN_PATHS = ["plugins"]
PLUGINS = ["tipue_search"]
DIRECT_TEMPLATES = (('index', 'tags', 'categories', 'authors', 'archives', 'search'))

PATH = 'content'
STATIC_PATHS = ['million','archive']
#ARTICLE_PATHS = ['blog']
ARTICLE_SAVE_AS = '{category}/{date:%Y}/{slug}.html'
ARTICLE_URL = '{category}/{date:%Y}/{slug}.html'
PAGE_SAVE_AS = '{slug}.html'
PAGE_URL = '{slug}.html'
DRAFT_SAVE_AS = 'draft/{slug}.html'
DRAFT_URL = 'draft/{slug}.html'

TIMEZONE = 'Asia/Shanghai'

DEFAULT_LANG = u'en'

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
SOCIAL = (('Github', 'https://github.com/nullne'),
        ('LinkedIn', 'https://www.linkedin.com/pub/le-yu/89/980/1a5'),
        ('豆瓣', 'http://www.douban.com/people/nullnes/'),
        ('微博', 'http://weibo.com/nullne'),)

DEFAULT_PAGINATION = 10

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True

DISPLAY_PAGES_ON_MENU = True
USE_FOLDER_AS_CATEGORY = True
DISPLAY_CATEGORIES_ON_MENU = False

#ARTICLE_ORDER_BY = 'date'
#PAGE_ORDER_BY = 'date'
REVERSE_CATEGORY_ORDER = True
NEWEST_FIRST_ARCHIVES = True
ARTICLE_EXCLUDES = ['archive']
