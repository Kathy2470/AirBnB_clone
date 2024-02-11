#!/usr/bin/python3
"""Defines unittests for models/place.py."""

import os
import models
import unittest
from datetime import datetime
from time import sleep
from models.place import Place


class TestPlace_instantiation(unittest.TestCase):
    """Unittests for testing instantiation of the Place class."""

    def test_no_args_instantiates(self):
        self.assertEqual(Place, type(Place()))

    def test_new_instance_stored_in_objects(self):
        self.assertIn(Place(), models.storage.all().values())

    def test_id_is_public_str(self):
        self.assertEqual(str, type(Place().id))

    def test_created_at_is_public_datetime(self):
        self.assertEqual(datetime, type(Place().created_at))

    def test_updated_at_is_public_datetime(self):
        self.assertEqual(datetime, type(Place().updated_at))

    def test_city_id_is_public_str(self):
        self.assertEqual(str, type(Place().city_id))

    def test_user_id_is_public_str(self):
        self.assertEqual(str, type(Place().user_id))

    def test_name_is_public_str(self):
        self.assertEqual(str, type(Place().name))

    def test_description_is_public_str(self):
        self.assertEqual(str, type(Place().description))

    def test_number_rooms_is_public_int(self):
        self.assertEqual(int, type(Place().number_rooms))

    def test_number_bathrooms_is_public_int(self):
        self.assertEqual(int, type(Place().number_bathrooms))

    def test_max_guest_is_public_int(self):
        self.assertEqual(int, type(Place().max_guest))

    def test_price_by_night_is_public_int(self):
        self.assertEqual(int, type(Place().price_by_night))

    def test_latitude_is_public_float(self):
        self.assertEqual(float, type(Place().latitude))

    def test_longitude_is_public_float(self):
        self.assertEqual(float, type(Place().longitude))

    def test_amenity_ids_is_public_list(self):
        self.assertEqual(list, type(Place().amenity_ids))

    # Additional tests can be added here...


class TestPlace_save(unittest.TestCase):
    """Unittests for testing save method of the Place class."""

    @classmethod
    def setUp(self):
        try:
            os.rename("file.json", "tmp")
        except IOError:
            pass

    def tearDown(self):
        try:
            os.remove("file.json")
        except IOError:
            pass
        try:
            os.rename("tmp", "file.json")
        except IOError:
            pass

    # Existing tests to be written...


class TestPlace_to_dict(unittest.TestCase):
    """Unittests for testing to_dict method of the Place class."""


if __name__ == "__main__":
    unittest.main()
