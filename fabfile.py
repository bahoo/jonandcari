from fabric.api import *

PROD_SERVER         = ['bahoo@bahoo.webfactional.com:22']
STAGING_SERVER      = ['bahoo@bahoo.webfactional.com:22']
PROJECT_DIRECTORY   = '/home/bahoo/webapps/jonandcari/jonandcari.repo'
NEW_PYTHON_PATH     = "/home/bahoo/webapps/jonandcari/lib/python2.7"


def production():
    env.hosts = PROD_SERVER
    env.forward_agent = True


def staging():
    env.hosts = STAGING_SERVER
    env.forward_agent = True


def deploy():
    with cd(PROJECT_DIRECTORY):
        run("git pull origin master")
        run("./manage.py collectstatic --noinput")
        run("./manage.py syncdb")
        run("./manage.py migrate rsvp")
        run('touch jonandcari/wsgi.py')
