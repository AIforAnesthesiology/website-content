#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals
from datetime import date

#
# Site specific variables
# Please update these to customize the website.
#
AUTHOR = "AI for Anesthesiology"
SITENAME = "Elisabeth-TweeSteden Ziekenhuis"
SITENAME_SHORT = "ETZ"
SITE_REPO = "website-etz"
SITE_GROUP = "etz"

# Home page and social settings
SITELEAD = """
Introtekst...
"""
SITE_PICTURE = "images/general/logo-etz.jpg"
HOME_IMAGE = "images/general/logo-etz.jpg"
# HOME_IMAGE_CAPTION = ''
TWITTER_URL = None
FOOTER_TEXT = ''
TOP_DOMAIN = '<a href="https://anesthesiologie.nl">NVA</a>'
PARENT_DOMAIN = (
    '<a href="https://www.aiforanesthesiology.nl">AI for Anesthesiology</a>'
)

# What sections to show in the nav bar
NAV_SECTIONS = [
    #{"name": "Highlights", "url": "highlights", "icon": "megaphone"},
    {"name": "Members", "url": "members", "icon": "users"},
    {"name": "Research", "url": "research", "icon": "folder"},
    {"name": "Vacancies", "url": "vacancies", "icon": "vacancies"},
    #{"name": "Publications", "url": "publications", "icon": "file-text-o", "hidden": 95},
    #{"name": "Thesis Gallery", "url": "thesis-gallery", "icon": "book", "hidden": 95},
    #{"name": "Contact", "url": "contact", "icon": "envelope-o", "hidden": 95},
]

# Whether to show breadcrumbs on the page
ENABLE_BREADCRUMBS = True

# What sections to show on homepage (current options that you customizable: {section_name: custom_name})
HOME_SECTIONS = {
    "Highlights": "Highlights",
    "Vacancies": "Vacancies",
    "Research": "Research",
}
# URLs
SITEURL = "https://etz.aiforanesthesiology.nl"
IMGURL = SITEURL
EDIT_CONTENT_URL = (
    "https://github.com/AIforAnesthesiology/website-content/edit/master/{file_path}"
)

#
# Non-content variables
# In general these values do not have to be changed.
#
PATH = "content"
RELATIVE_URLS = False

# Show pdf request on publication pages
ENABLE_PUBLICATION_PDF_REQUEST = False

TIMEZONE = "Europe/Amsterdam"
DEFAULT_LANG = "EN"
ARTICLE_TRANSLATION_ID = None
PAGE_TRANSLATION_ID = None

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

CURRENTYEAR = date.today().year
TODAY = date.today()
LINKS = ()
DEFAULT_PAGINATION = 10

# URL settings
BIBKEYS_SRC = "content/dict_pubs.json"
PAGE_URL = "{slug}/"
PAGE_SAVE_AS = "{slug}/index.html"
SLUGIFY_SOURCE = "basename"

ARTICLE_URL = "highlights/{slug}/"
ARTICLE_SAVE_AS = "highlights/{slug}/index.html"

TAGS_SAVE_AS = ""
TAG_SAVE_AS = ""
CATEGORY_URL = ""
CATEGORY_SAVE_AS = ""
CATEGORIES_SAVE_AS = ""

ARCHIVES_SAVE_AS = ""

SITEMAP_SAVE_AS = "sitemap.xml"
INDEX_SAVE_AS = "highlights/index.html"
ARTICLE_TYPE = "Highlights"

# Theme settings
THEME = "../radboudumc-template"
DIRECT_TEMPLATES = ["index", "archives", "sitemap"]

# Plugins
PLUGIN_PATHS = ["../plugins"]
PLUGINS = [
    "bibtex",
    "bibtex_loader",
    "edit_url",
    "hierarchy",
    "fileutil",
    "bootstrapify",
    "imgutil",
    "inline_extend",
    "content_aggregator",
]
