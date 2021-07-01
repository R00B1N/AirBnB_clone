#!/usr/bin/python3
"""
unittests for Place class
"""
import unittest
from models.place import Place
from models.base_model import BaseModel


class testfile(unittest.TestCase):
    """ unittests for Place class """
    def test_inheritance(self):
        """ checks if it inherits from BaseModel """
        self.assertTrue(issubclass(Place, BaseModel))
