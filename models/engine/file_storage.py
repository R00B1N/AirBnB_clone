#!/usr/bin/python3
"""
This module contains FileStorage class
"""
import json
from models.amenity import Amenity
from models.base_model import BaseModel
from models.city import City
from models.place import Place
from models.review import Review
from models.state import State
from models.user import User

class FileStorage:
    """
    serializes instances to a JSON file and deserializes JSON file to instances
    """
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """ returns the dictionary __objects """
        return FileStorage.__objects

    def new(self, obj):
        """ sets in __objects the obj with key <obj class name>.id """
        a = obj.__class__.__name__ + "." + str(obj.id)
        FileStorage.__objects[a] = obj

    def save(self):
        """ serializes __objects to the JSON file (path: __file_path """
        with open(FileStorage.__file_path, "w", encoding="utf-8") as o:
            x = {}
            for a, b in FileStorage.__objects.items():
                x[a] = b.to_dict()
                f = json.dumps(x)
                o.write(f)

    def reload(self):
        """ deserializes the JSON file to __objects (only if the JSON file (__file_path) exists """
        try:
            with open(FileStorage.__file_path, "r") as o:
                datos = json.load(o)
                for b in datos.values():
                    mi_clase = b["__class__"]
                    mi_clase = eval(mi_clase)
                    obj = mi_clase(**v)
                    self.new(obj)
        except:
            pass
