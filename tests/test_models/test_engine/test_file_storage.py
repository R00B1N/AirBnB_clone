#!/usr/bin/python3
"""
Unittest class
"""
import unittest
from models.engine.file_storage import FileStorage

class archivo_prueba(unittest.TestCase):
    """ A file storage class """
    def prob_obj(self):
        """ checking the object """
        almacenamiento = FileStorage()
        objetos = almacenamiento.all()
        for b in objetos.values():
            self.assertTrue(b != dict)
