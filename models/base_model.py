#!/usr/bin/python3
"""Defines the BaseModel class."""
import models
from uuid import uuid4
from datetime import datetime


class BaseModel:
    """Represents the basemodel for our project"""

    def __init__(self, *args, **kwargs):
        """Initialize a new instance."""

        self.id = str(uuid4())
        self.created_at = datetime.today()
        self.updated_at = datetime.today()

        if kwargs:
            for key, value in kwargs.items():
                if (key != '__class__'):
                    setattr(self, key, value)

                    if 'created_at' in kwargs:
                        self.created_at = datetime.strptime(
                                kwargs['created_at'], '%Y-%m-%dT%H:%M:%S.%f')

                    if 'updated_at' in kwargs:
                        self.updated_at = datetime.strptime(
                                kwargs['updated_at'], '%Y-%m-%dT%H:%M:%S.%f')
        else:
            models.storage.new(self)

    def save(self):
        """Updates the updated_at attribute with curr."""
        self.updated_at = datetime.now()
        models.storage.save()

    def to_dict(self):
        """Returns a dictionary containing all keys/values
        of __dict__ of the instance"""
        dictionary = self.__dict__.copy()
        dictionary['__class__'] = self.__class__.__name__
        dictionary['created_at'] = self.created_at.isoformat()
        dictionary['updated_at'] = self.updated_at.isoformat()
        return dictionary

    def __str__(self):
        """str representation of instance"""
        class_name = self.__class__.__name__
        return "[{}] ({}) {}".format(class_name, self.id, self.__dict__)
