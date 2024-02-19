#!/usr/bin/python3
"""Creates State module"""

from models.base_model import BaseModel


class State(BaseModel):
    """State class"""

    name = ""

    def __init__(self, *args, **kwargs):
        """Initializes attributes for the State class"""
        super().__init__(*args, **kwargs)
