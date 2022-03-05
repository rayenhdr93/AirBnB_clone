#!/usr/bin/python3
"""Def BaseModel"""
import json
from models.base_model import BaseModel

class FileStorage:
    '''FileStorage'''
    __file_path = 'objects.json'
    __objects = {}
    def all(self):
        return (self.__objects)

    def new(self, obj):
        if obj:
            self.__objects["{}.{}".format(BaseModel.__name__, BaseModel.id)] = obj

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
                class_name = key.split(',')[0]
                self.__objects[key] = eval(class_name)(**value) 
        except BaseException:
            pass
