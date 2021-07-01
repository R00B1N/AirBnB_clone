#!/usr/bin/python3
"""
unittests for Review class
"""
import unittest
from models.review import Review
from models.base_model import BaseModel


class testfile(unittest.TestCase):
    """ unittests for Review class """
    def test_inheritance(self):
        """ checks if it inherits from BaseModel """
        self.assertTrue(issubclass(Review, BaseModel))
