#!/usr/bin/python3
""" Base """
import uuid
from datetime import datetime
import models


class BaseModel:
"""BaseModel class"""

    def __init__(self, id=None, created_at=None):
        if id is not None:
            self.id = id
        else:
            self.id = str(uuid.uuid4())
        if created_at is not None:
            self.created_at = datetime.now()
        self.updated_at = datetime.now()
    def __str__(self):
        return "[{}} ({}) {}".format(
            type(self).__name__, self.id, self.__dict__)
    def to_dict(self):
        obj_dict = self.__dict__.copy()
        obj_dict['__class__'] = type(self).__name__
        obj_dict['created_at'] = self.created_at.isoformat()
        obj_dict['updated_at'] = self.updated_at.isoformat()
        return obj_dict
    def save(self):
        self.updated_at = datetime.now()
