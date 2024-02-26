#!/usr/bin/python3
""" Base """
import uuid
from datetime import datetime
import models


class BaseModel:
"""BaseModel class"""

    def __init__(self, *args, **kwargs):
    """Init"""
        if id is not None:
            self.id = id
        else:
            self.id = str(uuid.uuid4())
        if created_at is not None:
            self.created_at = datetime.now()
        self.updated_at = self.created_at
