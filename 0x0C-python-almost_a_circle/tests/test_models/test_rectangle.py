#!/usr/bin/python3
"""
Testing "rectangle" module
"""


import unittest
from models.base import Base
from models.rectangle import Rectangle


class TestRectangle(unittest.TestCase):
    """Testing Rectangle Class"""

    def setUp(self):
        """Setting Up all TestCases"""
        Base._Base__nb_objects = 0

    def test_valid_input(self):
        """testing valid input"""
        rec = Rectangle(1, 1)
        self.assertEqual(rec.width, 1)
        self.assertEqual(rec.height, 1)
        rec = Rectangle(1, 2, 3)
        self.assertEqual(rec.width, 1)
        self.assertEqual(rec.height, 2)
        self.assertEqual(rec.x, 3)

    def test_invalid_input(self):
        """testing invalid input"""
        with self.assertRaises(ValueError):
            r = Rectangle(1, -10)
        with self.assertRaises(ValueError):
            r = Rectangle(-81, -10)
        with self.assertRaises(ValueError):
            r = Rectangle(1, 1, -4)
        with self.assertRaises(ValueError):
            r = Rectangle(1, 1, -4, -4)
        with self.assertRaises(ValueError):
            r = Rectangle(1, 1, 4, -4)
        with self.assertRaises(TypeError):
            r = Rectangle("one", 5)
        with self.assertRaises(TypeError):
            r = Rectangle(1, 2, "three")

    def test_area(self):
        """Testing area method"""
        r = Rectangle(1, 2)
        self.assertEqual(r.area(), 2)
        r = Rectangle(1, 1)
        self.assertEqual(r.area(), 1)
        r = Rectangle(1, 2, 3, 4)
        self.assertEqual(r.area(), 2)
        r = Rectangle(1, 2, 3, 4, 5)
        self.assertEqual(r.area(), 2)

    def test_str(self):
        r = Rectangle(1, 2, 0, 0, 5)
        self.assertTrue(str(print(r)))
