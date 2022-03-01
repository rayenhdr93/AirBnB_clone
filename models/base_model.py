#!/usr/bin/python3
"""Def BaseModel"""
from uuid import uuid4
import uuid
from datetime import datetime


class BaseModel:
    '''BaseModel'''
    def __init__(self):
        '''__init__'''
        self.id = str(uuid.uuid4())
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
        return self.__dict__
