#!/usr/bin/python3
"""File Storeage class"""
import json
from models.base_model import BaseModel

class FileStorage():

    __file_path = "file.json"
    __objects = {}

    def all(self):
        """retrieve __objects"""
        return FileStorage.__objects

    def new(self, obj):
        """Add Object to __objects"""
        key_str = "{}.{}".format(obj.__class__.__name__, obj.id)
        FileStorage.__objects[key_str] = obj

    def save(self):
        """Save __objects to __file_path"""
        with open(FileStorage.__file_path, "w", encoding="utf-8") as objFile:
            temp = {k: v.to_dict() for k, v in FileStorage.__objects.items()}
            json.dump(temp, objFile)

    def reload(self):
        """Load objects from __file_path"""
        try:
            with open(FileStorage.__file_path, "r", encoding="utf-8") as fileobj:
                temp = json.load(fileobj)
                for k, v in temp.items():
                    restoredObject = eval(v['__class__'])(**v)
                    FileStorage.__objects[k] = restoredObject
                    
        except FileNotFoundError:
            pass
