#!/usr/bin/python3
import os
import tarfile
import datetime


def do_pack():
    """
    packs web_static into versions folder
    Return: the path of the saved targz
    """
    time = datetime.datetime.now().strftime("%Y%m%d%H%M%S")
    packpath = './versions/web_static_' + str(time)
    print('Packing web_static to ' + packpath)
    if not os.path.exists('versions'):
        os.mkdir('versions')
    with tarfile.open(packpath, "w:gz") as tar:
        tar.add('web_static', arcname=os.path.basename('static'))
    return packpath
