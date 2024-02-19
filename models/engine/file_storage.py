#!/usr/bin/python3
"""Module for DataStorage class."""
import datetime as dt
import json
import os


class DataStorage:

    """Class for handling data storage and retrieval"""
    __data_file_path = "data.json"
    __data_objects = {}

    def get_all_data(self):
        """Returns all data objects"""
        return DataStorage.__data_objects

    def add_data(self, obj):
        """Adds a data object to the storage"""
        key = "{}.{}".format(type(obj).__name__, obj.id)
        DataStorage.__data_objects[key] = obj

    def save_data(self):
        """Serializes data objects to JSON file"""
        with open(DataStorage.__data_file_path, "w", encoding="utf-8") as file:
            d = {k: v.to_dict() for k, v in Filestorage.__objects.items()}
            json.dump(data_dict, file)

    def load_classes(self):
        """Returns a dictionary of valid classes and their references"""
        from models.base_model import BaseModel
        from models.user import User
        from models.state import State
        from models.city import City
        from models.amenity import Amenity
        from models.place import Place
        from models.review import Review

        classes = {
            "BaseModel": BaseModel,
            "User": User,
            "State": State,
            "City": City,
            "Amenity": Amenity,
            "Place": Place,
            "Review": Review
        }
        return classes

    def reload_data(self):
        """Reloads data objects from the stored file"""
        if not os.path.isfile(DataStorage.__data_file_path):
            return
        with open(DataStorage.__data_file_path, "r", encoding="utf-8") as file:
            data_dict = json.load(file)
            data_dict = {k: self.load_classes()[v["__class__"]](**v)
                        for k, v in data_dict.items()}
            DataStorage.__data_objects = data_dict

    def get_attributes(self):
        """Returns valid attributes and their types for each class"""
        attributes = {
            "BaseModel": {
                "id": str,
                "created_at": dt.datetime,
                "updated_at": dt.datetime
            },
            "User": {
                "email": str,
                "password": str,
                "first_name": str,
                "last_name": str
            },
            "State": {
                "name": str
            },
            "City": {
                "state_id": str,
                "name": str
            },
            "Amenity": {
                "name": str
            },
            "Place": {
                "city_id": str,
                "user_id": str,
                "name": str,
                "description": str,
                "number_rooms": int,
                "number_bathrooms": int,
                "max_guest": int,
                "price_by_night": int,
                "latitude": float,
                "longitude": float,
                "amenity_ids": list
            },
            "Review": {
                "place_id": str,
                "user_id": str,
                "text": str
            }
        }
        return attributes
