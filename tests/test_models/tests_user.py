#!/usr/bin/python3
""" Base Class Test Cases"""
import unittest
from datetime import datetime
from models.user import User


class TestUser(unittest.TestCase):
    """Test cases for User class"""

    def test_getvalues(self):
        obj1 = User()
        self.assertIsNotNone(obj1.first_name)
        self.assertIsNotNone(obj1.last_name)
        self.assertIsNotNone(obj1.email)
        self.assertIsNotNone(obj1.password)
        obj2 = User()
        obj1.first_name = "Jacob"
        self.assertNotEqual(obj2.first_name, obj1.first_name)
