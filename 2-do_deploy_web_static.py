#!/usr/bin/python3
from fabric.api import put, run, local, env
import os
import time

env.hosts = ['35.227.25.29', '35.237.11.121']


def do_pack():
    timestr = time.strftime("%Y%m%d%H%M%S")
    if os.path.exists('./versions') is False:
        local("mkdir versions")
    execute = "tar -cvzf ./versions/web_static_{}.tgz web_static".format(
        timestr)
    result = local(execute)
    if result.succeeded:
        return "versions/web_static_{}".format(timestr)
    else:
        return None


def do_deploy(archive_path):
    if (os.path.exists(archive_path) is False):
        return None

    name_ext = archive_path.split('/')[-1]
    name = name_ext.split('.')[0]
    put(archive_path, '/tmp')
    location = '/data/web_static/releases/'
    run('mkdir -p {}{}'.format(location, name))
    run('tar -xzf /tmp/{} -C {}{}/'.format(name_ext, location, name))
    run('rm /tmp/{}'.format(name_ext))
    run('mv {}{}/web_static/* {}{}/'.format(location, name, location, name))
    run('rm -rf {}{}/web_static'.format(location, name))
    run('rm -rf /data/web_static/current')
    res = run('ln -sf {}{}/ /data/web_static/current'.format(location, name))
    if res.succeeded:
        print("New version deployed!")
        return True
    else:
        return False
