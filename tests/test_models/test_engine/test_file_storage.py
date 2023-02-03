#!/usr/bin/python3
""" Base Class Test Cases"""
import unittest
from models.engine.file_storage import FileStorage


class TestFileStorage(unittest.TestCase):

    testObject = None

    def test_contructors(self):
        pass
    
    def setUp(self) -> None:
        testObject = FileStorage()
        testObject._FileStoreage__file_path = "testResults.txt"
        return super().setUp()
    
    def tearDown(self) -> None:
        return super().tearDown()