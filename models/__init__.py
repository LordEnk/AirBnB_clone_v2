#!/usr/bin/env python3
"""
initialises the models storage
"""
import os
from models.engine.db_storage import DBStorage
from models.engine.file_storage import FileStorage

storage = DBStorage() if os.getenv(
    'HBNB_TYPE_STORAGE') == 'db' else FileStorage()
"""A unique FileStorage/DBStorage instance for all models.
"""
storage.reload()

