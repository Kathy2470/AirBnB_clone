#!/usr/bin/python3
"""Defines the reload method of FileStorage class."""
import os
import json


class FileStorage:
    """Handles serialization and deserialization of instances to JSON file."""

    __file_path = "file.json"
    __objects = {}

    def reload(self):
        """Reloads the stored objects from the JSON file."""
        try:
            if not os.path.isfile(FileStorage.__file_path):
                return

            with open(FileStorage.__file_path, "r", encoding="utf-8") as file:
                obj_dict = json.load(file)
                for key, val in obj_dict.items():
                    _class = self.classes()[val['__class__']]
                    obj_instance = _class(**val)
                    FileStorage.__objects[key] = obj_instance
                    print(f"Reload object: {obj_instance}")

        except FileNotFoundError:
            pass

    def classes(self):
        """Returns a dictionary of available classes."""
        from models.base_model import BaseModel
        from models.state import State
        from models.city import City
        from models.amenity import Amenity
        from models.place import Place
        from models.review import Review
        return {
                "BaseModel": BaseModel,
                "State": State,
                "City": City,
                "Amenity": Amenity,
                "Place": Place,
                "Review": Review
            }
