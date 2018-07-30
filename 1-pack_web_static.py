#!/usr/bin/python3
from fabric.api import put, run, local
import os
import time

def do_pack():
    timestr = time.strftime("%Y%m%d%H%M%S")
    execute = "tar -cvzf web_static_{}.tgz web_static".format(timestr)
    if os.path.exists('./versions') is False:
        local("mkdir versions")
    local(execute + " -C ./versions")
