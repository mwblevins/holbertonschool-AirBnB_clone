#!/usr/bin/python3
"""File Storeage class"""
import json


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
        with open(FileStorage.__file_path, "w") as objFile:
            json.dump(objFile, objFile)

    def reload(self):
        """Load objects from __file_path"""
        try:
            with open(FileStorage.__file_path, "r") as fileobj:
                FileStorage.__objects = json.load(fileobj)
        except FileNotFoundError:
            pass
