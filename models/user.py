#!/usr/bin/python3
""" module wich contains the user class """
from models.base_model import BaseModel

class User(BaseModel):
    """ class that inherits from BaseMode """
    email = ""
    password = ""
    first_name = ""
    last_name = ""
