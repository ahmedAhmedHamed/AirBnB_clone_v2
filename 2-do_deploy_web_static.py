#!/usr/bin/python3
import os
import datetime
from fabric.api import *

env.hosts = ['33.222.11.33', '66.44.33.222']


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


def do_deploy():
    """
    packs web_static into versions folder
    Return: the path of the saved targz
    """
    path = do_pack()
    upload_path = f'/tmp/{path}'
    archive_filename_without_extension = os.path.split('.')[0]
    decompression_path = '/data/web_static/releases/' + archive_filename_without_extension
    if path is None:
        return False
    put(path, upload_path)
    run(f"tar zxvf {upload_path} -C {decompression_path})
    run(f"rm {upload_path}")
    run("rm /data/web_static/current")
    run(f"ln -sf {decompression_path} /data/web_static/current")
    return True


