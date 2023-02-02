#!/usr/bin/python3
"""Base Model for Airbnb Clone - The Console"""

import uuid
from datetime import datetime

class BaseModel:
    """Class defines all common attributes/methods"""
    def __init__ (self):
        self.id = str(uuid.uuid4())
        self.created_at = self.updated_at = datetime.now()

    def __str__(self):
        """Prints"""
        return "[{}] ({}) {}".format(self.__class__.__name__, self.id, self.__dict__)

    def save(self):
        """Updates to current time"""
        self.updated_at = datetime.now()

    def to_dict(self):
        """Dictionary of key/values"""
        obj_dict = self.__dict__.copy()
        obj_dict['__class__'] = self.__class__.__name__
        obj_dict['created_at'] = self.created_at.isoformat()
        obj_dict['updated_at'] = self.updated_at.isoformat()
        return obj_dict
