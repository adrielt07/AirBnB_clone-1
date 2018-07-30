#!/usr/bin/python3
from fabric.api import put, run, local
import os
import time


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
