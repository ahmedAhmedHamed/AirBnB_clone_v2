#!/usr/bin/python3
import os
import tarfile
import datetime
from fabric.api import local


def do_pack():
    """
    packs web_static into versions folder
    Return: the path of the saved targz
    """
    if not os.path.exists('web_static'):
        return None
    time = datetime.datetime.now().strftime("%Y%m%d%H%M%S")
    packpath = './versions/web_static_' + str(time) + '.tgz'
    local("mkdir -p versions")
    local("tar -czvf {} web_static".format(packpath))
    return packpath
