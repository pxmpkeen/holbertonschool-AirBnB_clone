#!/usr/bin/python3
import unittest
import os
from models.file_storage import FileStorage
from models.base_model import BaseModel


class TestFileStorage(unittest.TestCase):
"""TestFileStorage"""
    def setUp(self):
        self.storage = FileStorage()
        self.base_model = BaseModel()
        
        def tearDown(self):
            if os.path.exists(self.storage._FileStorage__file_path):
                os.remove(self.storage._FileStorage__file_path)
                
        def test_all(self):
            self.assertEqual(self.storage.all(), {})
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
                                                                                                                      
