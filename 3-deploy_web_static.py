#!/usr/bin/python3
'''generates a .tgz archive from the contents of the web_static\
folder of your AirBnB Clone repo, using the function do_pack'''
from fabric.api import local, put, run, env
from os import path
from datetime import datetime

env.hosts = ["{}@35.196.187.53".format(env.user),
             "{}@34.75.244.141".format(env.user)]

env.tgz = ""

def do_pack():
    """ Create directory if doesn't exist and backup folder web_static """
    time = str(datetime.now()).split(".")[0].replace(
        ":", "").replace(" ", "").replace("-", "")
    if not path.exists("versions"):
        local("mkdir -p versions")
    local("tar -czf versions/web_static_{}.tgz web_static".format(time))
    env.tgz = ("versions/web_static_{}.tgz".format(time))

def do_deploy(archive_path):
    '''distributes an archive to your web servers'''
    if not path.exists(archive_path):
        return(False)

    try:
        # upload tgz file to servers
        put(archive_path, "/tmp/")

        # variables to be used
        tgzname = archive_path.split("/")[-1]
        webpath = "/data/web_static/releases/{}/".format(tgzname[:-4])
        tmpath = "/tmp/{}".format(tgzname)
        sympath = "/data/web_static/current"

        # create folder to tgz file
        run("mkdir -p {}".format(webpath))

        # uncompressed tgz file
        run("tar -xzf {} -C {}".format(tmpath, webpath))

        # remove tgz
        run("rm {}".format(tmpath))

        # move all uncompressed files
        run("mv {}web_static/* {}".format(webpath, webpath))

        # remove web_static folder
        run("rm -rf {}/web_static".format(webpath))

        # remove the symbolic link
        run("rm -rf {}".format(sympath))

        # create new symbolic link
        run("ln -s {} {}".format(webpath, sympath))
        return(True)

    except:
        return(False)

def deploy():
    '''creates and distributes an archive to your web servers'''
    if env.tgz == "":
        do_pack()
    return(do_deploy(env.tgz))
