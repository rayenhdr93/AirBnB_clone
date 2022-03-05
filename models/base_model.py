#!/usr/bin/python3
"""Def BaseModel"""
from uuid import uuid4
from datetime import datetime


class BaseModel:
    '''BaseModel'''


    def __init__(self, *args, **kwargs):
        '''__init__'''


        if kwargs:
            for key, value in kwargs.items():
                if key == 'created_at' or key == 'updated_at':
                    value = datetime.strptime(value, "%Y-%m-%dT%H:%M:%S.%f")
                if key != '__class__':
                    setattr(self, key, value)
        else:
            self.id = str(uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()

    def __str__(self):
        '''__str__'''


        return "[{}] ({}) {}".format(self.__class__.__name__,
                                     self.id, self.__dict__)

    def save(self):
        '''save'''


        self.updated_at = datetime.now()

    def to_dict(self):
        '''dict'''


        new = self.__dict__.copy()
        new['created_at'] = datetime.now().isoformat("T")
        new['updated_at'] = datetime.now().isoformat("T")
        new['__class__'] = type(self).__name__
        return new
