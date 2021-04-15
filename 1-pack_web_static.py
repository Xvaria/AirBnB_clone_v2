#!/usr/bin/python3
""" Module for storing the do_pack() method. """


def do_pack():
    """ Packs the contents of the /web_static directory in .tgz """
    from fabric.api import local
    from datetime import datetime
    from os import path, getcwd

    if path.exists("./versions") is False:
        local("mkdir versions")

    time = datetime.now().strftime("%Y%m%d%H%M%S")
    file_name = "versions/web_static_{}.tgz".format(time)
    cwd = getcwd()
    try:
        local("tar -cvzf {} web_static".format(file_name))
        return(cwd + "/" + file_name)
    except Exception as e:
        return(None)
