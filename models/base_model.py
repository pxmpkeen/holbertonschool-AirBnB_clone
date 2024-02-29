#!/usr/bin/python3
"""
Implementation of Base Model for all classes
"""
from uuid import uuid4
import datetime


class BaseModel:
    """Base model for all classes"""

    def __init__(self, *args, **kwargs) -> None:
        """Creating an instance"""
        from models import storage
        if kwargs:
            kwargs['created_at'] = datetime.datetime.fromisoformat(
                kwargs['created_at']
            )
            kwargs['updated_at'] = datetime.datetime.fromisoformat(
                kwargs['updated_at']
            )
            kwargs.pop('__class__')
            self.__dict__ = kwargs
        else:
            self.id = str(uuid4())
            self.created_at = datetime.datetime.now()
            self.updated_at = datetime.datetime.now()
            storage.new(self)

    def __str__(self) -> str:
        """Overriding string representation of class"""
        return "[{:s}] ({:s}) {}".format(
                self.__class__.__name__, self.id, self.__dict__)

    def to_dict(self) -> dict:
        obj_dict = self.__dict__.copy()
        obj_dict['created_at'] = str(self.created_at.isoformat())
        obj_dict['updated_at'] = str(self.updated_at.isoformat())
        return obj_dict | {'__class__': self.__class__.__name__}

    def save(self) -> None:
        from models import storage
        self.updated_at = datetime.datetime.now()
        storage.save()
