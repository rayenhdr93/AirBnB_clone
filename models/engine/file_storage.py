#!/usr/bin/python3
"""Def BaseModel"""
import json
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review


class FileStorage:
    '''FileStorage'''
    __file_path = 'file.json'
    __objects = {}

    def all(self):
        return (self.__objects)

    def new(self, obj):
        if obj:
            key = obj.__class__.__name__ + '.' + obj.id
            self.__objects[key] = obj

    def save(self):
        save_dict = {}
        for key, value in self.__objects.items():
            save_dict[key] = value.to_dict()
        with open(self.__file_path, "w", encoding="UTF-8") as f:
            json.dump(save_dict, f)

    def reload(self):
        try:
            with open(self.__file_path, "r", encoding="UTF-8") as f:
                obj = json.load(f)
            for key, value in obj.items():
                class_name = key.split('.')[0]
                self.__objects[key] = eval(class_name)(**value)
        except FileNotFoundError:
            pass
