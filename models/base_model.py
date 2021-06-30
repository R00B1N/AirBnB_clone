#!/usr/bin/python3
"""
Module wich contains the BaseModel class
"""
from datetime import datetime
import models
import uuid


class BaseModel:
    """
    The class BaseModel defines all common attributes/methods for other classes
    """
    def __init__(self, *args, **kwargs):
        """ method instantiation """
        self.id = str(uuid.uuid4())
        self.created_at = datetime.now()
        self.updated_at = datetime.now()
        if kwargs:
            for a, b in kwargs.items():
                if a == 'created_at':
                    self.created_at = datetime.strptime(
                            b,
                            '%Y-%m-%dT%H:%M:%S.%f')
                elif a == 'updated_at':
                    self.updated_at = datetime.strptime(
                            b,
                            '%Y-%m-%dT%H:%M:%S.%f')
                elif k == '__class__':
                    self.__class__.__name__ = b
                else:
                    setattr(self, a, b)
        else:
            models.storage.new(self)

    def __str__(self):
        """ print the object """
        return "[{}] ({}) {}".format(self.__class__.__name__,
                self.id, self.__dict__)

    def save(self):
        """
        updates the public instance attribute updated_at with the current datetime
        """
        self.updated_at = datetime.now()
        models.storage.new(self)
        models.storage.save()

    def to_dict(self):
        """
        returns a dictionary containing all keys/values of __dict__ of the instance
        """
        x = {}
        for a, b in self.__dict__.items():
            if a != 'created_at' and a != 'updated_at':
                x[a] = b
        x['__class__'] = self.__class__.__name__
        x['created_at'] = self.created_at.isoformat()
        x['updated_at'] = self.updated_at.isoformat()
        return x
