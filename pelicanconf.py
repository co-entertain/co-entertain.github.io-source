#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = u'nullne'
SITENAME = u'NULLNE'
SITEURL = ''
THEME = 'themes/nullne'

PATH = 'content'
STATIC_PATHS = ['downloads']
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
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None

# Blogroll
LINKS = (('Pelican', 'http://getpelican.com/'),
         ('Python.org', 'http://python.org/'),
         )

# Social widget
SOCIAL = (('Github', 'https://github.com/nullne'),
        ('Weibo', 'http://weibo.com/nullne'),)

DEFAULT_PAGINATION = 10

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True

DISPLAY_PAGES_ON_MENU = True
USE_FOLDER_AS_CATEGORY = True
DISPLAY_CATEGORIES_ON_MENU = False
