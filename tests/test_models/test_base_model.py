#!/usr/bin/python3
import unittest
from datetime import datetime
from models.base_model import BaseModel


class TestBaseModel(unittest.TestCase):
    def setUp(self):
        self.base_model = BaseModel()

    def test_save(self):
        initial_updated_at = self.base_model.updated_at
        self.base_model.save()
        self.assertNotEqual(initial_updated_at, self.base_model.updated_at)

    def test_to_dict(self):
        obj_dict = self.base_model.to_dict()
        self.assertIn('__class__', obj_dict)
        self.assertEqual(obj_dict['__class__'], 'BaseModel')
        self.assertIn('id', obj_dict)
        self.assertEqual(obj_dict['id'], self.base_model.id)
        self.assertIn('created_at', obj_dict)
        self.assertEqual(obj_dict['created_at'], self.base_model.created_at.isoformat())
        self.assertIn('updated_at', obj_dict)
        self.assertEqual(obj_dict['updated_at'], self.base_model.updated_at.isoformat())

    def test_self_id(self):
        self.assertIsInstance(self.base_model.id, str)

    def test_self_created_at(self):
        self.assertIsInstance(self.base_model.created_at, datetime)

    def test_str(self):
        expected_str = "[BaseModel] ({}) {}".format(self.base_model.id, self.base_model.__dict__)
        self.assertEqual(str(self.base_model), expected_str)


if __name__ == '__main__':
    unittest.main()
