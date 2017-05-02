#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = 'gardenunez'
SITENAME = 'Educacion canina en positivo'
SITEURL = ''

TIMEZONE = 'Europe/Madrid'
DEFAULT_LANG = 'es'


PATH = 'content'

# pages
PAGE_PATHS = ['pages']
PAGE_URL = 'pages/{slug}.html'
PAGE_ORDER_BY = 'page-order'

# Disable feed generation
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# disable generation of tag-related pages
# http://docs.getpelican.com/en/stable/faq.html#is-pelican-only-suitable-for-blogs
TAGS_SAVE_AS = ''
TAG_SAVE_AS = ''


LOAD_CONTENT_CACHE = False

# Blogroll
# LINKS = (('Pelican', 'http://getpelican.com/'),
#          ('Python.org', 'http://python.org/'),
#          ('Jinja2', 'http://jinja.pocoo.org/'),
#          ('You can modify those links in your config file', '#'),)
#
# Social widget
SOCIAL = (('facebook', 'http://facebook.com/JuanmaSF7'),)

# DEFAULT_PAGINATION = 10

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True
