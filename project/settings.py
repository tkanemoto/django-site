from settings_default import *

import sys
sys.path.append(os.path.join(BASE_DIR, 'apps'))

TEMPLATES[0]['DIRS'] = [
	os.path.join(BASE_DIR, 'templates'),
]

STATICFILES_DIRS = (
    os.path.join(BASE_DIR, 'static'),
)

STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
    'compressor.finders.CompressorFinder',
)

COMPRESS_ROOT = os.path.join(BASE_DIR, 'static')
COMPRESS_OUTPUT_DIR = 'compressed'
COMPRESS_CSS_FILTERS = [
    #'compressor.filters.css_default.CssAbsoluteFilter',
    #'compressor.filters.datauri.CssDataUriFilter',
    'compressor.filters.css_default.CssRelativeFilter',
    'compressor.filters.cssmin.rCSSMinFilter',
]
COMPRESS_DATA_URI_MAX_SIZE = 1000000

INSTALLED_APPS += (
    'portfolios',
    'storages',
    'ordered_model',
)

INSTALLED_APPS += (
    # Dependencies
    'django.contrib.sites',
    'tagging',
    'treemenus',
    'django_gravatar',
    'django_comments',
    # Apps
    'base',
    'player',
    'dj_torrent',
    # Basic Apps
    'basic.blog',
    #'basic.bookmarks',
    #'basic.books',
    'basic.comments',
    #'basic.events',
    #'basic.flagging',
    #'basic.groups',
    'basic.inlines',
    #'basic.invitations',
    #'basic.media',
    #'basic.messages',
    #'basic.movies',
    'basic.music',
    'basic.people',
    #'basic.places',
    'basic.profiles',
    #'basic.relationships',
    'basic.tools',
    'compressor',
)

COMMENTS_APP = 'basic.comments'
AUTH_PROFILE_MODULE = 'profiles.Profile'

SITE_ID = 1

#TEMPLATE_DEBUG = DEBUG

if DEBUG:
    MEDIA_ROOT = BASE_DIR
    MEDIA_URL = '/media/'

ADMIN_SITE_HEADER = 'Django administration'

FILE_UPLOAD_HANDLERS = [
    'portfolios.uploadhandlers.CompressImageUploadHandler',
    'django.core.files.uploadhandler.TemporaryFileUploadHandler',
]

FILE_UPLOAD_MAX_MEMORY_SIZE = 262144000
