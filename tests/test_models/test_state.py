#!/usr/bin/python3
import unittest
from models.state import State
from datetime import datetime
from models import storage


class TestState(unittest.TestCase):
    def setUp(self):
        self.state = State()
    def test_instance(self):
        self.assertIsInstance(self.state, State)
        self.assertIsInstance(self.state, BaseModel)
    def test_attributes(self):
        self.assertTrue(hasattr(self.state, 'name'))
        self.assertTrue(hasattr(self.state, 'id'))
        self.assertTrue(hasattr(self.state, 'created_at'))
        self.assertTrue(hasattr(self.state, 'updated_at')) 
    def test_defaults(self):
        self.assertEqual(self.state.name, "")
        self.assertIsInstance(self.state.created_at, datetime)
        self.assertIsInstance(self.state.updated_at, datetime)
    def test_to_dict(self):
        state_dict = self.state.to_dict()
        self.assertEqual(state_dict['__class__'], 'State')
        self.assertIsInstance(state_dict['created_at'], str)
        self.assertIsInstance(state_dict['updated_at'], str)
        self.assertEqual(state_dict['name'], self.state.name)
    def test_save(self):
        initial_updated_at = self.state.updated_at
        self.state.save()
        self.assertNotEqual(initial_updated_at, self.state.updated_at)
    def tearDown(self):
        storage.reload()
