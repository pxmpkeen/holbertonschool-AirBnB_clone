#!/usr/bin/python3
import unittest
from models.amenity import Amenity
from datetime import datetime
from models import storage


class TestAmenity(unittest.TestCase):

    def setUp(self):
        self.amenity = Amenity()

    def test_instance(self):
        self.assertIsInstance(self.amenity, Amenity)
        self.assertIsInstance(self.amenity, BaseModel)

    def test_attributes(self):
        self.assertTrue(hasattr(self.amenity, 'name'))
        self.assertTrue(hasattr(self.amenity, 'id'))
        self.assertTrue(hasattr(self.amenity, 'created_at'))
        self.assertTrue(hasattr(self.amenity, 'updated_at'))

    def test_defaults(self):
        self.assertEqual(self.amenity.name, "")
        self.assertIsInstance(self.amenity.created_at, datetime)
        self.assertIsInstance(self.amenity.updated_at, datetime)

    def test_to_dict(self):
        amenity_dict = self.amenity.to_dict()
        self.assertEqual(amenity_dict['__class__'], 'Amenity')
        self.assertIsInstance(amenity_dict['created_at'], str)
        self.assertIsInstance(amenity_dict['updated_at'], str)
        self.assertEqual(amenity_dict['name'], self.amenity.name)

    def test_save(self):
        initial_updated_at = self.amenity.updated_at
        self.amenity.save()
        self.assertNotEqual(initial_updated_at, self.amenity.updated_at)
