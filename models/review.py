#!/usr/bin/python3
"""Defines the Review class."""

from models.base_model import BaseModel


class Review(BaseModel):
    """Represents a review of a place."""

    def __init__(self, *args, **kwargs):
        """Initialize Review instance."""
        super().__init__(*args, **kwargs)
        self.place_id = ""
        self.user_id = ""
        self.text = ""

    def to_dict(self):
        """Return dictionary representation of Review."""
        obj_dict = super().to_dict()
        obj_dict.update({
            "place_id": self.place_id,
            "user_id": self.user_id,
            "text": self.text
        })
        return obj_dict
