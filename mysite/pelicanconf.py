#!/usr/bin/env python
# -*- coding: utf-8 -*- #

AUTHOR = 'shangfr'
SITENAME = "Shangfr"
SITETITLE = "My Webite"
SITESUBTITLE = "使用pelican制作的静态网站"
SITEDESCRIPTION = "主题-Flex - The minimalist Pelican theme."

SITEURL = ""
SITELOGO = '/images/logo.png'
FAVICON = '/images/favicon.ico'
BROWSER_COLOR = "#007d65"
PYGMENTS_STYLE = "monokai"

PATH = 'content'

THEME = "Flex"

TIMEZONE = 'Europe/Paris'

DEFAULT_LANG = 'Chinese (Simplified)'

I18N_TEMPLATES_LANG = "en"
DEFAULT_LANG = "en"
OG_LOCALE = "en_US"
LOCALE = "en_US"

DATE_FORMATS = {
    "en": "%B %d, %Y",
}

FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

USE_FOLDER_AS_CATEGORY = False
MAIN_MENU = True
HOME_HIDE_TAGS = True

SOCIAL = (
    ("github", "https://github.com/shangfr"),
    ("rss", "/blog/feeds/all.atom.xml"),
)

MENUITEMS = (
    ("Archives", "/archives.html"),
    ("Categories", "/categories.html"),
    ("Tags", "/tags.html"),
)

CC_LICENSE = {
    "name": "Creative Commons Attribution-ShareAlike",
    "version": "4.0",
    "slug": "by-sa",
}

COPYRIGHT_YEAR = 2021
DEFAULT_PAGINATION = 10

#DISQUS_SITENAME = "flex-pelican"
#ADD_THIS_ID = "ra-55adbb025d4f7e55"

STATIC_PATHS = ["images"]



THEME_COLOR_AUTO_DETECT_BROWSER_PREFERENCE = True
THEME_COLOR_ENABLE_USER_OVERRIDE = True

USE_LESS = True
