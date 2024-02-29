#!/usr/bin/python3
"""Amenity"""
from models.base_model import BaseModel


class Amenity(BaseModel):
    """Class Amenity"""
    name = ""

    def __init__(self, *args, **kwargs):
        """Creating an instance"""
        super().__init__(*args, **kwargs)
