#!/usr/bin/python3
"""
Unittest for BaseModel class
"""
import unittest
from models.base_model import BaseModel
from datetime import datetime


class testbase(unittest.TestCase):
    """
    unittests for BaseModel class
    """
    def test_attributes(self):
        """
        check attributes
        """
        b1 = BaseModel()
        b2 = BaseModel()
        self.assertNotEqual(b1.id, b2.id)
        b1.name = "Mariem"
        self.assertEqual(b1.name, "Mariem")
        self.assertTrue(isinstance(b1.created_at, datetime))
        self.assertTrue(isinstance(b2.updated_at, datetime))
        self.assertTrue(type(b1.id) is str)
        self.assertTrue(type(b1.to_dict()), dict)
