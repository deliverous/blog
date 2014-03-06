#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = u'Olivier Albiez et Thomas Clavier'
SITENAME = u'Deliverous Blog'
SITEURL = 'http://blog.deliverous.com'
THEME = './theme'


TIMEZONE = 'Europe/Paris'

DEFAULT_LANG = u'fr'

FILENAME_METADATA = '(?P<slug>(?P<date>\d{4}-\d{2}-\d{2})_.*)'
USE_FOLDER_AS_CATEGORY = True
DELETE_OUTPUT_DIRECTORY = True
FEED_ALL_ATOM = 'feeds/all.atom.xml'


# Blogroll
#LINKS =  (('Pelican', 'http://getpelican.com/'),
#          ('Python.org', 'http://python.org/'),
#          ('Jinja2', 'http://jinja.pocoo.org/'),
#          ('You can modify those links in your config file', '#'),)

# Social widget
#SOCIAL = (('Azae', 'http://azae.net'),)
#          ('Another social link', '#'),)




# Theme customisation
MENUITEMS = (('L\'équipe', 'http://deliverous.com/#equipe'),)
DISPLAY_CATEGORIES_ON_MENU = False
DISPLAY_PAGES_ON_MENU = True

DISPLAY_CATEGORIES_ON_SIDEBAR = True
DISPLAY_TAGS_ON_SIDEBAR = True
DISPLAY_RECENT_POSTS_ON_SIDEBAR = True

DISPLAY_ARTICLE_INFO_ON_INDEX = False


DISPLAY_BREADCRUMBS = False

# Extensions
ASCIIDOC_OPTIONS = []
MD_EXTENSIONS = ['codehilite(css_class=highlight)','extra', 'admonition']
#, 'markdown_checklist.extension'

PLUGIN_PATH = "plugins"
PLUGINS = ["related_posts", "gzip_cache", "simple_footnotes"]

# static content
STATIC_PATHS = ['images']
