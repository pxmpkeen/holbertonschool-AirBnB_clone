#!/usr/bin/python3
""" Base """
import uuid
from datetime import datetime
import models


class BaseModel:
"""BaseModel class"""

    def __init__(self, *args, **kwargs):
    """Init"""
        if kwargs:
            for key, value in kwargs.items():
