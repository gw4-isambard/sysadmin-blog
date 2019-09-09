#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = 'Isambard sysadmins'
SITENAME = 'GW4 Isambard'
SITEURL = '.'

PATH = 'content'

TIMEZONE = 'Europe/London'

DEFAULT_LANG = 'en'

THEME = 'theme/pelican-blue'

FAVICON = '/logo/raisingsteam.favicon.png'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

DISPLAY_CATEGORIES_ON_MENU = True

MENUITEMS = (
    ('Documentation', 'https://gw4-isambard.github.io/docs/'),
    ('GW4', 'https://gw4.ac.uk/isambard/'),
)

DEFAULT_PAGINATION = False

RELATIVE_URLS = True
