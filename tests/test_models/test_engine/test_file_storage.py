#!/usr/bin/python3
""" Base Class Test Cases"""
import unittest
from models.engine.file_storage import FileStorage
from models.base_model import BaseModel

class TestFileStorage(unittest.TestCase):

    testObject = None

    def test_contructors(self):
        self.testObject.reload()
        self.assertEqual(len(self.testObject.all()), 0)
        obj = BaseModel()
        self.testObject.new(obj)
        self.assertEqual(len(self.testObject.all()),1)
        pass
    
    def setUp(self) -> None:
        self.testObject = FileStorage()
        return super().setUp()
    
    def tearDown(self) -> None:
        return super().tearDown()