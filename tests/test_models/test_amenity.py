#!/usr/bin/python3
"""
unittests for Amenity class
"""
import unittest
from models.amenity import Amenity
from models.base_model import BaseModel


class testfile(unittest.TestCase):
    """ unittests for Amenity class """
    def test_inheritance(self):
        """ checks if it inherits from BaseModel """
        self.assertTrue(issubclass(Amenity, BaseModel))
