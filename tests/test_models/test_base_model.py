#!/usr/bin/python3
""" Base Class Test Cases"""
import unittest
from datetime import datetime
from models.base_model import BaseModel

class TestBaseModel(unittest.TestCase):
    """TASK 1 UNIT TESTS"""
    def test_bas_mod_id(self):
        bm1 = BaseModel()
        self.assertIsInstance(bm1.id, str)

    def test_bas_mod_crt(self):
        bm1 = BaseModel()
        self.assertIsInstance(bm1.created_at, datetime)

    def test_bas_mod_upd(self):
        bm1 = BaseModel()
        self.assertIsInstance(bm1.updated_at, datetime)

    def test_uwu_id(self):
        bm1 = BaseModel()
        bm2 = BaseModel()
        self.assertNotEqual(bm1.id, bm2.id)

    def test_ini_tim(self):
        bm1 = BaseModel()
        self.assertEqual(bm1.created_at, bm1.updated_at)

    def test_sav_upd_met(self):
        bm1 = BaseModel()
        created = bm1.created_at
        updated = bm1.updated_at
        bm1.save()
        self.assertEqual(bm1.created_at, created)
        self.assertNotEqual(bm1.updated_at, updated)

    def test_to_dict(self):
        bm1 = BaseModel()
        dict_model = bm1.to_dict()
        self.assertIsInstance(dict_model, dict)
        self.assertIsInstance(dict_model["updated_at"], str)
        self.assertIsInstance(dict_model["created_at"], str)

    def test_str_met(self):
        bm1 = BaseModel()
        self.assertIn(bm1.id, str(bm1))