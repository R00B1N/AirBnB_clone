#!/usr/bin/python3
"""
unittests for User class
"""
import unittest
from models.user import User
from models.base_model import BaseModel


class testfile(unittest.TestCase):
    """ unittests for User class """
    def test_inheritance(self):
        """ checks if it inherits from BaseModel """
        self.assertTrue(issubclass(User, BaseModel))
