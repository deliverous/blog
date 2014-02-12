#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = u'Olivier Albiez et Thomas Clavier'
SITENAME = u'Deliverous'
SITEURL = ''
THEME = './themes/blueidea'
# gum

TIMEZONE = 'Europe/Paris'

DEFAULT_LANG = u'fr'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None

# Blogroll
#LINKS =  (('Pelican', 'http://getpelican.com/'),
#          ('Python.org', 'http://python.org/'),
#          ('Jinja2', 'http://jinja.pocoo.org/'),
#          ('You can modify those links in your config file', '#'),)

# Social widget
#SOCIAL = (('Azae', 'http://azae.net'),)
#          ('Another social link', '#'),)

DEFAULT_PAGINATION = False

#INDEX_SAVE_AS = 'blog.html'
#MENUITEMS = (('Tags', SITEURL + '/tags.html'),)

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True

#PLUGIN_PATH = 'plugins'
#PLUGINS = ['pdf',]


# Theme customisation
PAGES_SORT_ATTRIBUTE = 'source_path'
DISPLAY_CATEGORIES_ON_SUBMENU = False
DISPLAY_CATEGORIES_ON_MENU = True



ASCIIDOC_OPTIONS = []


MD_EXTENSIONS = ['codehilite(css_class=highlight)','extra', 'admonition', 'markdown_checklist.extension']