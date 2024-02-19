#!/usr/bin/python3
"""Creates Amenity class"""

from models.base_model import BaseModel


class Amenity(BaseModel):
    """Amenity class"""

    name = ""

    def __init__(self, *args, **kwargs):
        """Initializes attributes for the Amenity class"""
        super().__init__(*args, **kwargs)
