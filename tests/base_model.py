#!/usr/bin/python3
import json
import uuid
from datetime import datetime


class BaseModel:
    """Defines the BaseModel class."""

    def __init__(self, *args, **kwargs):
        """Initialize BaseModel."""
        if kwargs:
            for key, value in kwargs.items():
                if key == "__class__":
                    continue
                if key == "created_at" or key == "updated_at":
                    value = datetime.strptime(value, "%Y-%m-%dT%H:%M:%S.%f")
                setattr(self, key, value)
        else:
            self.id = str(uuid.uuid4())
            self.created_at = self.updated_at = datetime.now()

    def save(self):
        """Update updated_at attribute."""
        self.updated_at = datetime.now()

    def to_dict(self):
        """Return dictionary representation of object."""
        obj_dict = self.__dict__.copy()
        obj_dict["__class__"] = self.__class__.__name__
        obj_dict["created_at"] = self.created_at.isoformat()
        obj_dict["updated_at"] = self.updated_at.isoformat()
        return obj_dict

    def __str__(self):
        """Return string representation of object."""
        return "[{}] ({}) {}".format(
            self.__class__.__name__, self.id, self.__dict__
        )

from models.base_model import BaseModel


class State(BaseModel):
    """State class that inherits from BaseModel."""
    name = ""
