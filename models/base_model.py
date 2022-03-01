#!/usr/bin/python3
"""Def BaseModel"""
from uuid import uuid4
from datetime import datetime


class BaseModel:
    '''BaseModel'''
    def __init__(self):
        '''__init__'''
        self.id = str(uuid4())
        self.created_at = datetime.today()
        self.updated_at = datetime.today()

    def __str__(self):
        '''__str__'''
        return "[{}] ({}) {}".format(self.__class__.__name__, self.id, self.__dict__)

    def save(self):
        '''save'''
        self.updated_at = datetime.today()

