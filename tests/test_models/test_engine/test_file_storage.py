#!/usr/bin/python3
import unittest
import os
import json
from models.base_model import BaseModel
from models.user import User
from models.engine.file_storage import FileStorage


class TestFileStorage(unittest.TestCase):
    def setUp(self):
        self.storage = FileStorage()
        self.base_model = BaseModel()
        
    def tearDown(self):
        if os.path.exists(self.storage._FileStorage__file_path):
            os.remove(self.storage._FileStorage__file_path)
            
    def test_all(self):
        self.assertEqual(len(self.storage.all()), 0)
        self.storage.new(self.base_model)
        self.assertEqual(len(self.storage.all()), 1)
        
    def test_save_and_reload(self):
        self.storage.new(self.base_model)
        self.storage.save()
        new_storage = FileStorage()
        new_storage.reload()
        self.assertEqual(len(new_storage.all()), 1)
        new_model = list(new_storage.all().values())[0]
        self.assertEqual(new_model.id, self.base_model.id)
            
    def test_new(self):
        self.assertEqual(len(self.storage.all()), 0)
        user = User()
        self.storage.new(user)
        self.assertEqual(len(self.storage.all()), 1)
        self.assertIn(f'{user.__class__.__name__}.{user.id}', self.storage.all())

    def test_save(self):
        self.storage.new(self.base_model)
        self.storage.save()
        with open(self.storage._FileStorage__file_path, 'r') as f:
            data = json.load(f)
            self.assertIn(f'{self.base_model.__class__.__name__}.{self.base_model.id}', data)
