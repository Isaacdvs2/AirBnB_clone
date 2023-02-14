#!/usr/bin/python3
"""Initializes the package"""
import os
import sys
from models.engine.file_storage import FileStorage

storage = FileStorage()
storage.reload()
