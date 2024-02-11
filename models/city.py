#!/usr/bin/python3
"""Defines the City class."""

from models.base_model import BaseModel


class City(BaseModel):
    """Represents a city."""

    def __init__(self, *args, **kwargs):
        """Initialize a new City."""
        super().__init__(*args, **kwargs)
        self.state_id = kwargs.get('state_id', "")
        self.name = kwargs.get('name', "")


if __name__ == "__main__":
    pass  
