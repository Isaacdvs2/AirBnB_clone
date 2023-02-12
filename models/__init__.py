#!/usr/bin/python3
"""Initializes the package"""
import os
import sys
sys.path.insert(0, os.path.dirname(os.getcwd()))
from models.engine.file_storage import FileStorage
storage = FileStorage()
storage.reload()
