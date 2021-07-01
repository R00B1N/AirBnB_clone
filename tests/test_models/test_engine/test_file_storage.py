#!/usr/bin/python3
"""
Unittest for FileStorage class
"""
import unittest
from models.engine.file_storage import FileStorage


class testfile(unittest.TestCase):
    """
    unittests for FileStorage class
    """
    def test_obj(self):
        """
        check obj
        """
        storage = FileStorage()
        objs = storage.all()
        for v in objs.values():
            self.assertTrue(v != dict)
