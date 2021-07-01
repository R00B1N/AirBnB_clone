#!/usr/bin/python3
"""
unittests for Amenity class
"""
import unittest
from models.amenity import Amenity
from models.base_model import BaseModel


class file_test(unittest.TestCase):
    """ unittests for Amenity class """
    def inherit_testing(self):
        """ function wich checks if it inherits is from BaseModel """
        self.assertTrue(issubclass(Amenity, BaseModel))
