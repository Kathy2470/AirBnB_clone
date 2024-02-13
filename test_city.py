#!/usr/bin/python3
"""Defines unittests for models/city.py."""

import os
import models
import unittest
from datetime import datetime
from time import sleep
from models.city import City


class TestCityInstantiation(unittest.TestCase):
    """Unittests for testing instantiation of the City class."""

    def test_inheritance(self):
        """Test if City inherits from BaseModel."""
        new_city = City()
        self.assertIsInstance(new_city, BaseModel)

    def test_attributes(self):
        """Test if City has the required attributes."""
        new_city = City()
        self.assertTrue(hasattr(new_city, 'state_id'))
        self.assertTrue(hasattr(new_city, 'name'))


class TestCitySave(unittest.TestCase):
    """Unittests for testing save method of the City class."""

    @classmethod
    def setUpClass(cls):
        try:
            os.rename("file.json", "tmp")
        except IOError:
            pass

    def tearDownClass(cls):
        try:
            os.remove("file.json")
        except IOError:
            pass
        try:
            os.rename("tmp", "file.json")
        except IOError:
            pass

    def test_one_save(self):
        city = City()
        sleep(0.05)
        first_updated_at = city.updated_at
        city.save()
        self.assertLess(first_updated_at, city.updated_at)

    # Add other save tests as required


class TestCityToDict(unittest.TestCase):
    """Unittests for testing to_dict method of the City class."""

    def test_to_dict_type(self):
        """Test if to_dict() returns a dictionary."""
        city = City()
        self.assertIsInstance(city.to_dict(), dict)

    # Add other to_dict tests as required


if __name__ == "__main__":
    unittest.main()
