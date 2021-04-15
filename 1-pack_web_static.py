#!/usr/bin/python3
'''generates a .tgz archive from the contents of the web_static\
folder of your AirBnB Clone repo, using the function do_pack'''
from fabric.api import local
from os import path
from datetime import datetime


def do_pack():
    '''Packing web_static to versions/web_static_20170314233357.tgz'''
    if not path.exists("versions"):
        local("mkdir versions")
    local("tar -czf versions/web_static_{}.tgz web_static".
          format(str(datetime.now()).split(".")[0].replace("-", "").
                 replace(" ", "").replace(":", "")))
