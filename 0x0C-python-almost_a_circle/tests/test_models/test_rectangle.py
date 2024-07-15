#!/usr/bin/python3
"""
Testing "rectangle" module
"""


import io
import sys
import unittest
from models.base import Base
from models.rectangle import Rectangle


class TestRectangle(unittest.TestCase):
    """Testing Rectangle Class"""

    @staticmethod
    def evaluate(obj, method):
        """return value"""
        oldstdout = sys.stdout
        newstdout = io.StringIO()
        sys.stdout = newstdout
        if method == "print":
            print(obj)
        else:
            obj.display()
        sys.stdout = oldstdout
        return newstdout.getvalue()

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
        r = Rectangle(1, 2, 1, 1, 88)
        self.assertEqual(r.width, 1)
        self.assertEqual(r.height, 2)
        self.assertEqual(r.x, 1)
        self.assertEqual(r.y, 1)
        self.assertEqual(r.id, 88)

    def test_v_input(self):
        """testing valid input"""
        Base._Base__nb_objects = 0
        r = Rectangle(1, 3)
        self.assertEqual(r.width, 1)
        self.assertEqual(r.height, 3)
        self.assertEqual(r.x, 0)
        self.assertEqual(r.y, 0)

    def test_invalid_input(self):
        """testing invalid input"""
        with self.assertRaises(ValueError):
            r = Rectangle(-1, 2)
        with self.assertRaises(ValueError):
            r = Rectangle(1, -2)
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
        with self.assertRaises(TypeError):
            r = Rectangle("1", 5)
        with self.assertRaises(TypeError):
            r = Rectangle(1, "5")
        with self.assertRaises(TypeError):
            r = Rectangle(1, 1, 4, "4")
        with self.assertRaises(ValueError):
            r = Rectangle(0, 6)
        with self.assertRaises(ValueError):
            r = Rectangle(4, 0)
        with self.assertRaises(ValueError):
            r = Rectangle(0, 0)
        with self.assertRaises(ValueError):
            r = Rectangle(0, 0, 0, 0)

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
        """testing object string"""
        r = Rectangle(1, 2, 0, 0, 5)
        st = "[Rectangle] (5) 0/0 - 1/2"
        output = self.evaluate(r, "print")
        self.assertEqual(st.rstrip(), output.rstrip())

    def test_display(self):
        """testing display method"""
        r = Rectangle(2, 3, 0, 0)
        output = self.evaluate(r, "display")
        val = "##\n##\n##\n"
        self.assertEqual(output, val)
        r = Rectangle(2, 3)
        output = self.evaluate(r, "display")
        val = "##\n##\n##\n"
        self.assertEqual(output, val)
        r = Rectangle(2, 3, 1)
        output = self.evaluate(r, "display")
        val = " ##\n ##\n ##\n"
        self.assertEqual(output, val)

    def test_to_dictionary(self):
        """testing to_dictionary method"""
        r = Rectangle(2, 3)
        val = {"id": r.id,
                "width": r.width,
                "height": r.height,
                "x": r.x,
                "y": r.y
                }
        self.assertEqual(r.to_dictionary(), val)

    def test_update(self):
        """Testing update methode"""
        r = Rectangle(2, 3)
        r.update(10)
        self.assertEqual(r.id, 10)
