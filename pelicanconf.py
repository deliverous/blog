#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals
from datetime import datetime

AUTHOR = u'Olivier Albiez et Thomas Clavier'
SITENAME = u'Blog Deliverous'
SITEURL = 'http://blog.deliverous.com'
THEME = './theme'
FAVICON = 'images/favicon.png'

# Pour avoir des urls reative en dev
RELATIVE_URLS = True

TIMEZONE = 'Europe/Paris'

DEFAULT_LANG = u'fr'

FILENAME_METADATA = '(?P<slug>(?P<date>\d{4}-\d{2}-\d{2})\..*)'
PATH_METADATA = '(?P<category>[^/]*)'
USE_FOLDER_AS_CATEGORY = False
DELETE_OUTPUT_DIRECTORY = True
FEED_ALL_ATOM = 'feeds/all.atom.xml'

# Blogroll
#LINKS =  (('<i class="fa fa-envelope"></i> Mailing list Deliverous', 'http://ml.deliverous.com/mailman/listinfo/deliverous'),
#          ('<i class="fa fa-github"></i> Deliverous', 'https://github.com/Deliverous'),
#          ('<i class="fa fa-rss"></i> RSS', 'http://blog.deliverous.com/feeds/all.atom.xml'),)


#LINKS =  (('Pelican', 'http://getpelican.com/'),
#          ('Python.org', 'http://python.org/'),
#          ('Jinja2', 'http://jinja.pocoo.org/'),
#          ('You can modify those links in your config file', '#'),)

# Social widget
SOCIAL = (
          ('<i class="fa fa-github"></i> GitHub', 'https://github.com/Deliverous'),
          ('<i class="fa fa-twitter"></i> Twitter', 'https://twitter.com/DeliverousCom'),
          ('<i class="fa fa-rss"></i> RSS', 'http://blog.deliverous.com/feeds/all.atom.xml'),
          ('<i class="fa fa-envelope"></i> Contact', 'mailto:contact@deliverous.com'),
          ('<i class="fa fa-envelope"></i> Mailing list Deliverous', 'http://ml.deliverous.com/mailman/listinfo/deliverous'),
         )


DISQUS_SITENAME = 'blogdeliverous'


# Theme customisation
LOCALE = ('fr_FR.utf8')
DEFAULT_DATE_FORMAT = "%Y - %m - %d"
#DATE_FORMATS = {
#    'en': ('en_US','%a, %d %b %Y'),
#}


BOOTSTRAP_NAVBAR_INVERSE = True

MENUITEMS = (
        ('<span class="fa fa-cloud"></span> Hébergement', 'http://deliverous.com/hebergement'),
        ('<span class="fa fa-graduation-cap"></span> Service', 'http://deliverous.com/service'),
        ('<span class="fa fa-group"></span> Équipe', 'http://deliverous.com/team'),
        ('<i class="fa fa-github"></i> GitHub', 'https://github.com/Deliverous'),
        ('<i class="fa fa-twitter"></i> Twitter', 'https://twitter.com/DeliverousCom'),
        ('<i class="fa fa-envelope"></i> Contact', 'mailto://contact@deliverous.com'),
        ('<i class="fa fa-rss"></i> RSS', 'http://blog.deliverous.com/feeds/all.atom.xml'),
        ('<i class="fa fa-tag"></i> Tags', '/tags.html'),
        ('<i class="fa fa-folder-open"></i> Categories', '/categories.html'),
    )
DISPLAY_CATEGORIES_ON_MENU = False
DISPLAY_PAGES_ON_MENU = True

HIDE_SIDEBAR = True
DISPLAY_CATEGORIES_ON_SIDEBAR = True
DISPLAY_TAGS_ON_SIDEBAR = True
DISPLAY_RECENT_POSTS_ON_SIDEBAR = True

DISPLAY_ARTICLE_INFO_ON_INDEX = True

DISPLAY_BREADCRUMBS = False

DEFAULT_PAGINATION = 12

# Extensions
ASCIIDOC_OPTIONS = []
MD_EXTENSIONS = ['codehilite(css_class=highlight)','extra', 'admonition']
#, 'markdown_checklist.extension'

PLUGIN_PATHS = ["plugins"]
PLUGINS = ["related_posts", "gzip_cache", "simple_footnotes", "thumbnailer", "sitemap"]

IMAGE_PATH = 'images'
THUMBNAIL_DIR = 'images/thumbnails'
THUMBNAIL_SIZES = {
    '_icon': '75',
    '_square': '360',
    '_wide': '750x?',
#    'thumbnail_wide': '150x?',
#    'thumbnail_tall': '?x150',
}


# static content
STATIC_PATHS = ['images']

SITEMAP = {
    'format': 'xml',
    'priorities': {
        'articles': 0.5,
        'indexes': 0.5,
        'pages': 0.5
    },
    'changefreqs': {
        'articles': 'monthly',
        'indexes': 'daily',
        'pages': 'monthly'
    }
}

GITHUB_USER = 'Deliverous'

TAGS_URL = 'tags.html'

UPDATE_DATE = datetime.today()

PYGMENTS_STYLE = 'friendly'
