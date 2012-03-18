from fabric.api import *
from fabric.contrib.project import *

env.local_static_root = '/tmp/kylefuller.co.uk'
env.remote_static_root = '/srv/http/'

def build(output='output'):
    local('pelican -d -s settings.py -o {} content'.format(output))

def deploy():
    build(env.local_static_root)
    rsync_project(remote_dir=env.remote_static_root,
                  local_dir=env.local_static_root,
                  delete=True)
    local('rm -r {}'.format(env.local_static_root))
