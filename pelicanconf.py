#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = 'Juanmadog'
SITENAME = 'juanmadog'
SITEURL = ''

TIMEZONE = 'Europe/Madrid'
DEFAULT_LANG = 'es'


PATH = 'content'

# pages
PAGE_PATHS = ['pages']
PAGE_URL = 'pages/{slug}.html'
PAGE_ORDER_BY = 'page-order'
PAGE_EXCLUDES = ['pages/exclude']

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

THEME = 'themes/pelican-bootstrap3'
JINJA_ENVIRONMENT = {'extensions': ['jinja2.ext.i18n']}

# plugins
PLUGIN_PATHS = ['./pelican-plugins']
PLUGINS = ['i18n_subsites']


# Blogroll
# LINKS = (('Pelican', 'http://getpelican.com/'),
#          ('Python.org', 'http://python.org/'),
#          ('Jinja2', 'http://jinja.pocoo.org/'),
#          ('You can modify those links in your config file', '#'),)
#
# Social widget
SOCIAL = (('facebook', 'https://www.facebook.com/juanmadog'),)

# DEFAULT_PAGINATION = 10

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True

# About
ABOUT_ME='Soy un enamorado de los animales pero en especial de los perros, tal es mi entusiasmo que he querido estudiar y formarme para poder ayudarles. Soy Educador Canino, Ayudante Técnico Veterinario (ATV) y lo último que he estudiado (de momento) es Fisioterapia y Rehabilitación en pequeños animales. Colaboro con el Centro de Protección Animal Mancomunidad Henares Jarama, realizando labores de Educador (terapias frente ansiedad y miedos) y ATV (vacunaciones, desparasitaciones y cirugías entre otras actividades).'
