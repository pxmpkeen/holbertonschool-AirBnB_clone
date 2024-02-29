#!/usr/bin/python3
import unittest
from models.review import Review
from datetime import datetime
from models import storage


class TestReview(unittest.TestCase):

    def setUp(self):
        self.review = Review()

    def test_instance(self):
        self.assertIsInstance(self.review, Review)
        self.assertIsInstance(self.review, BaseModel)

    def test_attributes(self):
        self.assertTrue(hasattr(self.review, 'place_id'))
        self.assertTrue(hasattr(self.review, 'user_id'))
        self.assertTrue(hasattr(self.review, 'text'))
        self.assertTrue(hasattr(self.review, 'id'))
        self.assertTrue(hasattr(self.review, 'created_at'))
        self.assertTrue(hasattr(self.review, 'updated_at'))

    def test_defaults(self):
        self.assertEqual(self.review.place_id, "")
        self.assertEqual(self.review.user_id, "")
        self.assertEqual(self.review.text, "")
        self.assertIsInstance(self.review.created_at, datetime)
        self.assertIsInstance(self.review.updated_at, datetime)

    def test_to_dict(self):
        review_dict = self.review.to_dict()
        self.assertEqual(review_dict['__class__'], 'Review')
        self.assertIsInstance(review_dict['created_at'], str)
        self.assertIsInstance(review_dict['updated_at'], str)
        self.assertEqual(review_dict['place_id'], self.review.place_id)
        self.assertEqual(review_dict['user_id'], self.review.user_id)
        self.assertEqual(review_dict['text'], self.review.text)

    def test_save(self):
        initial_updated_at = self.review.updated_at
        self.review.save()
        self.assertNotEqual(initial_updated_at, self.review.updated_at)
