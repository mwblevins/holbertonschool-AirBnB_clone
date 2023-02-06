#!/usr/bin/python3
""" Base Class Test Cases"""
import unittest
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
