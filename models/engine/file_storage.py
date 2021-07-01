#!/usr/bin/python3
'''
Class that stores files
'''

import json
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review


class FileStorage:
    '''
    File storage class
    '''
    __file_path = "file.json"
    __objects = {}

    def all(self):
        '''
        Returns the dictionary __objects
        '''
        return self.__objects

    def new(self, obj):
        '''
        Sets in __objects the obj with key <obj class name>.id
        '''
        key = "{}.{}".format(obj.__class__.__name__, obj.id)
        self.__objects[key] = obj

    def save(self):
        '''
        Serializes __objects to the JSON file (path: __file_path)
        '''
        sv = {}
        for key, value in self.__objects.items():
            sv[key] = value.to_dict()
        with open(self.__file_path, "w") as file:
            json.dump(sv, file, indent="")

    def reload(self):
        '''
        deserializes the JSON file to __objects (only if the JSON file
        (__file_path) exists ; otherwise, do nothing.
        If the file doesn’t exist, no exception should be raised)
        '''
        try:
            with open(self.__file_path, "r") as file:
                for j, value in (json.load(file)).items():
                    self.__objects[j] = eval(value["__class__"] + "(**value)")
        except FileNotFoundError:
            pass
