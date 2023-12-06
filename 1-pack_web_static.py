#!/usr/bin/python3
import os
import tarfile
import datetime


def do_pack():
    """
    packs web_static into versions folder
    Return: the path of the saved targz
    """
    if not os.path.exists('versions'):
        os.mkdir('versions')
    time = datetime.datetime.now().strftime("%Y%m%d%H%M%S")
    with tarfile.open('./versions/web_static_' + str(time), "w:gz") as tar:
        tar.add('web_static', arcname=os.path.basename('static'))
    return './versions/web_static_' + str(time)
