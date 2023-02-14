#!/usr/bin/python3
"""Initializes the package"""
import os
import sys
from models.engine.file_storage import FileStorage

sys.path.insert(0, os.path.dirname(os.getcwd()))

storage = FileStorage()
storage.reload()
