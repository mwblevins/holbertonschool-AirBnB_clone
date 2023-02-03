#!/usr/bin/python3
"""Base Model for Airbnb Clone - The Console"""
import uuid
from datetime import datetime
from models import storage


class BaseModel:
    """Class defines all common attributes/methods"""
    def __init__(self, *args, **kwargs):
        self.created_at = self.updated_at = datetime.now()
        self.id = str(uuid.uuid4())
        if kwargs != {}:
            for k, v in kwargs.items():
                if k != "__class__":
                    setattr(self, k, v)
        else:
            storage.new(self)
        self.created_at = self.created_at \
            if type(self.created_at) is not str else\
            datetime.strptime(self.created_at, "%Y-%m-%dT%H:%M:%S.%f")
        self.updated_at = self.updated_at \
            if type(self.updated_at) is not str else \
            datetime.strptime(self.updated_at, "%Y-%m-%dT%H:%M:%S.%f")

    def __str__(self):
        """Prints"""
        return "[{}] ({}) {}".format(self.__class__.__name__,
                                     self.id, self.__dict__)

    def save(self):
        """Updates to current time"""
        self.updated_at = datetime.now()
        storage.save()

    def to_dict(self):
        """Dictionary of key/values"""
        obj_dict = self.__dict__.copy()
        obj_dict['__class__'] = self.__class__.__name__
        obj_dict['created_at'] = self.created_at.isoformat()
        obj_dict['updated_at'] = self.updated_at.isoformat()
        return obj_dict
