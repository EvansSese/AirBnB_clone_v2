#!/usr/bin/python3
"""This module instantiates an object of class FileStorage"""
from os import getenv
from models.engine.file_storage import FileStorage

storage_type = getenv("HBNB_TYPE_STORAGE")

storage = FileStorage()
storage.reload()
