from .base import *

# Django settings for jonandcari project.

DEBUG = True
TEMPLATE_DEBUG = DEBUG

EMAIL_HOST = 'localhost'
EMAIL_PORT = 1025

# Absolute path to the directory static files should be collected to.
# Don't put anything in this directory yourself; store your static files
# in apps' "static/" subdirectories and in STATICFILES_DIRS.
# Example: "/var/www/example.com/static/"
STATIC_ROOT = '/Users/Cari/Documents/GitHub/jonandcari/staticfiles/'

# Additional locations of static files
STATICFILES_DIRS = (
    '/Users/Cari/Documents/GitHub/jonandcari/static/',
)

TEMPLATE_DIRS = (
    '/Users/Cari/Documents/GitHub/jonandcari/templates/'
)
