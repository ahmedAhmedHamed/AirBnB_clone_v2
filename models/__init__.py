#!/usr/bin/python3
"""This module instantiates an object of class FileStorage"""
import os

from .state import State
from .city import City
from .user import User
from .review import Review
from .place import Place
from .amenity import Amenity

STORAGE = os.environ.get('HBNB_TYPE_STORAGE')

if STORAGE == 'db':
    from models.engine.db_storage import DBStorage
    storage = DBStorage()
    storage.reload()
else:
    from models.engine.file_storage import FileStorage
    storage = FileStorage()
    storage.reload()