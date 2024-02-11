#!/usr/bin/python3
"""Defines unittests for models/amenity.py.

Unittest classes:
    TestAmenity_instantiation
    TestAmenity_save
    TestAmenity_to_dict
"""
import os
import models
import unittest
from datetime import datetime
from time import sleep
from models.amenity import Amenity


class TestAmenityInstantiation(unittest.TestCase):
    """Unittests for testing instantiation of the Amenity class."""

    def test_inheritance(self):
        """Test if Amenity inherits from BaseModel."""
        new_amenity = Amenity()
        self.assertIsInstance(new_amenity, BaseModel)

    def test_attributes(self):
        """Test if Amenity has the required attributes."""
        new_amenity = Amenity()
        self.assertTrue(hasattr(new_amenity, 'name'))
        self.assertEqual(new_amenity.name, "")

    # Add other instantiation tests as required


class TestAmenitySave(unittest.TestCase):
    """Unittests for testing save method of the Amenity class."""

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
        am = Amenity()
        sleep(0.05)
        first_updated_at = am.updated_at
        am.save()
        self.assertLess(first_updated_at, am.updated_at)

    # Add other save tests as required


class TestAmenityToDict(unittest.TestCase):
    """Unittests for testing to_dict method of the Amenity class."""

    def test_to_dict_type(self):
        """Test if to_dict() retu#!/usr/bin/python3
"""Defines unittests for models/amenity.py.


Unittest classes:
    TestAmenity_instantiation
    TestAmenity_save
    TestAmenity_to_dict
"""
import os
import models
import unittest
from datetime import datetime
from time import sleep
from models.amenity import Amenity


class TestAmenityInstantiation(unittest.TestCase):
    """Unittests for testing instantiation of the Amenity class."""

    def test_inheritance(self):
        """Test if Amenity inherits from BaseModel."""
        new_amenity = Amenity()
        self.assertIsInstance(new_amenity, BaseModel)

    def test_attributes(self):
        """Test if Amenity has the required attributes."""
        new_amenity = Amenity()
        self.assertTrue(hasattr(new_amenity, 'name'))
        self.assertEqual(new_amenity.name, "")

    # Add other instantiation tests as required


class TestAmenitySave(unittest.TestCase):
    """Unittests for testing save method of the Amenity class."""

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
        am = Amenity()
        sleep(0.05)
        first_updated_at = am.updated_at
        am.save()
        self.assertLess(first_updated_at, am.updated_at)



class TestAmenityToDict(unittest.TestCase):
    """Unittests for testing to_dict method of the Amenity class."""

    def test_to_dict_type(self):
        """Test if to_dict() returns a dictionary."""
        am = Amenity()
        self.assertIsInstance(am.to_dict(), dict)


if __name__ == "__main__":
    unittest.main()ain__":
    unittest.main()
