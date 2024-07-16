#!/usr/bin/python3
"""
Testing "rectangle" module
"""


import io
import sys
import os
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
        r = Rectangle(2, 3)
        r.update(10, 1)
        self.assertEqual(r.id, 10)
        self.assertEqual(r.width, 1)
        r = Rectangle(2, 3)
        r.update(10, 1, 1)
        self.assertEqual(r.id, 10)
        self.assertEqual(r.width, 1)
        self.assertEqual(r.height, 1)
        r = Rectangle(2, 2, 2, 2, 700)
        r.update(10, 1, 1, 1)
        self.assertEqual(r.id, 10)
        self.assertEqual(r.width, 1)
        self.assertEqual(r.height, 1)
        self.assertEqual(r.x, 1)
        r = Rectangle(2, 2, 2, 2, 700)
        r.update(10, 1, 1, 1, 1)
        self.assertEqual(r.id, 10)
        self.assertEqual(r.width, 1)
        self.assertEqual(r.height, 1)
        self.assertEqual(r.x, 1)
        self.assertEqual(r.y, 1)
        r = Rectangle(2, 2, 2, 2, 700)
        r.update(**{"id": 4})
        self.assertEqual(r.id, 4)
        r = Rectangle(2, 2, 2, 2, 700)
        r.update(**{"id": 4, "width": 4})
        self.assertEqual(r.id, 4)
        self.assertEqual(r.width, 4)
        r = Rectangle(2, 2, 2, 2, 700)
        r.update(**{"id": 4, "width": 4, "height": 4})
        self.assertEqual(r.id, 4)
        self.assertEqual(r.width, 4)
        self.assertEqual(r.height, 4)
        r = Rectangle(2, 2, 2, 2, 700)
        r.update(**{"id": 4, "width": 4, "height": 4, "x": 4})
        self.assertEqual(r.id, 4)
        self.assertEqual(r.width, 4)
        self.assertEqual(r.height, 4)
        self.assertEqual(r.x, 4)
        r = Rectangle(2, 2, 2, 2, 700)
        r.update(**{"id": 4, "width": 4, "height": 4, "x": 4, "y": 4})
        self.assertEqual(r.id, 4)
        self.assertEqual(r.width, 4)
        self.assertEqual(r.height, 4)
        self.assertEqual(r.x, 4)
        self.assertEqual(r.y, 4)

    def test_create(self):
        """Testing create method"""
        d = {"id": 4}
        r = Rectangle.create(**d)
        self.assertEqual(r.id, 4)
        d = {"id": 4, "width": 4}
        r = Rectangle.create(**d)
        self.assertEqual(r.id, 4)
        self.assertEqual(r.width, 4)
        d = {"id": 4, "width": 4, "height": 4}
        r = Rectangle.create(**d)
        self.assertEqual(r.id, 4)
        self.assertEqual(r.width, 4)
        self.assertEqual(r.height, 4)
        d = {"id": 4, "width": 4, "height": 4, "x": 4}
        r = Rectangle.create(**d)
        self.assertEqual(r.id, 4)
        self.assertEqual(r.width, 4)
        self.assertEqual(r.height, 4)
        self.assertEqual(r.x, 4)
        d = {"id": 4, "width": 4, "height": 4, "x": 4, "y": 4}
        r = Rectangle.create(**d)
        self.assertEqual(r.id, 4)
        self.assertEqual(r.width, 4)
        self.assertEqual(r.height, 4)
        self.assertEqual(r.x, 4)
        self.assertEqual(r.y, 4)

    def test_save_to_file(self):
        """testing save_to_file method"""
        Rectangle.save_to_file([])
        self.assertTrue(os.path.exists("Rectangle.json"))
        if os.path.exists("Rectangle.json"):
            with open("Rectangle.json", encoding="UTF-8") as ff:
                content = ff.read()
            self.assertEqual(content, "[]")
        os.remove("Rectangle.json")
        Rectangle.save_to_file(None)
        self.assertTrue(os.path.exists("Rectangle.json"))
        if os.path.exists("Rectangle.json"):
            with open("Rectangle.json", encoding="UTF-8") as ff:
                content = ff.read()
            self.assertEqual(content, "[]")
        os.remove("Rectangle.json")
        obj = Rectangle(1, 4)
        objects = [obj]
        Rectangle.save_to_file(objects)
        self.assertTrue(os.path.exists("Rectangle.json"))
        if os.remove("Rectangle.json"):
            with open("Rectangle.json", encoding="UTF-8") as ff:
                content = ff.read()
            val = '[{"id": 13, "width": 1, "height": 1, "x": 0, "y": 0}]'
            self.assertEqual(content, val)

    def test_load_from_file(self):
        """testing load_from_file"""
        obj = Rectangle(6, 6, 6, 6, 98)
        objects = [obj]
        Rectangle.save_to_file(objects)
        content = Rectangle.load_from_file()
        for a, b in zip(sorted(content), sorted(objects)):
            self.assertEqual(a.__str__(), b.__str__())
