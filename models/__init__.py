#!/usr/bin/python3
"""Init file for the models module."""

from models.engine.file_storage import FileStorage

storage = FileStorage()
storage.reload()
