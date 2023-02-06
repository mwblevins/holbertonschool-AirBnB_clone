#!/usr/bin/python3
""" Base Class Test Cases"""
import unittest
import json
from models.engine.file_storage import FileStorage
from models.base_model import BaseModel


class TestFileStorage(unittest.TestCase):

    testObject = None

    def test_contructors(self):
        self.testObject.reload()
        start_count = len(self.testObject.all())
        obj = BaseModel()
        self.testObject.new(obj)
        self.assertEqual(len(self.testObject.all()), start_count + 1)
        pass

    def setUp(self) -> None:
        self.testObject = FileStorage()
        return super().setUp()

    def tearDown(self) -> None:
        return super().tearDown()

    def setUp(self):
        """initialize objects and file storage instance"""
        self.obj1 = {"id": 1, "name": "Test1"}
        self.obj2 = {"id": 2, "name": "Test2"}
        self.fs = FileStorage()

    def test_all(self):
        """Test if all method retrieves objects correctly"""
        self.fs.new(self.obj1)
        self.fs.new(self.obj2)
        self.assertDictEqual(self.fs.all(), {"dict.1": self.obj1, "dict.2": self.obj2})

    def test_new(self):
        """Test if new method adds object to __objects correctly"""
        self.fs.new(self.obj1)
        self.assertDictEqual(self.fs.all(), {"dict.1": self.obj1})

    def test_remove(self):
        """Test if remove method deletes the correct object from __objects"""
        self.fs.new(self.obj1)
        self.fs.new(self.obj2)
        self.fs.remove("dict.1")
        self.assertDictEqual(self.fs.all(), {"dict.2": self.obj2})

    def test_save(self):
        """Test if save method saves objects to file correctly"""
        self.fs.new(self.obj1)
        self.fs.new(self.obj2)
        self.fs.save()
        with open(FileStorage.__file_path, "r", encoding="utf-8") as fileobj:
            data = json.load(fileobj)
            self.assertDictEqual(data, {"dict.1": self.obj1, "dict.2": self.obj2})

    def test_reload(self):
        """Test if reload method loads objects from file correctly"""
        self.fs.new(self.obj1)
        self.fs.new(self.obj2)
        self.fs.save()
        self.fs.__objects = {}
        self.fs.reload()
        self.assertDictEqual(self.fs.all(), {"dict.1": self.obj1, "dict.2": self.obj2})
