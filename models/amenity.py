#!/usr/bin/python3
"""Amenity"""
from models.base_model import BaseModel


class Amenity(BaseModel):
    name = ""
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)