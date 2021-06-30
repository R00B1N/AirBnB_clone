#!/usr/bin/python3
""" module wich contains the place class """
from models.base_model import BaseModel

class Place(BaseModel):
    """ place class """
    city_id = ""
    user_id = ""
    name = ""
    description = ""
    number_rooms = 0
    number_bathrooms = 0
    price_by_night = 0
    latitude = 0.0
    longitude = 0.0
    amenity_ids = []
