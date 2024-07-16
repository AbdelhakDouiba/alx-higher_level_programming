#!/usr/bin/python3
"""
Testing "square" module
"""


import io
import sys
import os
import unittest
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square


class TestSquareClass(unittest.TestCase):
    """TestSuite for Square Class"""

    @staticmethod
    def evaluate(obj, method):
        """return value for print or display()"""

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
        """setting up testCases"""

        Base._Base__nb_objects = 0

    def test_valid_input(self):
        """testing valid input"""
        s = Square(7)
        self.assertEqual(s.size, 7)
        self.assertEqual(s.x, 0)
        self.assertEqual(s.y, 0)
        s = Square(14, 2)
        self.assertEqual(s.size, 14)
        self.assertEqual(s.x, 2)
        s = Square(14, 2, 1)
        self.assertEqual(s.size, 14)
        self.assertEqual(s.x, 2)
        self.assertEqual(s.y, 1)
        s = Square(14, 2, 1, 55)
        self.assertEqual(s.size, 14)
        self.assertEqual(s.x, 2)
        self.assertEqual(s.y, 1)
        self.assertEqual(s.id, 55)

    def test_invalid_input(self):
        """testing invalid input"""
        with self.assertRaises(ValueError):
            s = Square(-7)
        with self.assertRaises(ValueError):
            s = Square(14, -2)
        with self.assertRaises(ValueError):
            s = Square(14, 2, -2)
        with self.assertRaises(ValueError):
            s = Square(-14, -2, -2, -2)
        with self.assertRaises(ValueError):
            s = Square(0)
        with self.assertRaises(TypeError):
            s = Square("Zero")
        with self.assertRaises(TypeError):
            s = Square("0")
        with self.assertRaises(TypeError):
            s = Square([0])
        with self.assertRaises(TypeError):
            s = Square(1, "twenty")
        with self.assertRaises(TypeError):
            s = Square(1, "20")
        with self.assertRaises(TypeError):
            s = Square(1, 20, "5")

    def test_str(self):
        """testing the string of the object"""
        s = Square(4, 1, 1, 1)
        the_str = self.evaluate(s, "print")
        expected = f"[Square] ({s.id}) {s.x}/{s.y} - {s.size}"
        self.assertEqual(the_str.rstrip(), expected)

    def test_to_dictionary(self):
        """testing to_dictionary method"""
        s = Square(4, 1, 1, 1)
        output = s.to_dictionary()
        expected = {"id": s.id,
                    "size": s.width,
                    "x": s.x,
                    "y": s.y
                    }
        self.assertEqual(output, expected)

    def test_update(self):
        """testing update method"""
        s = Square(4, 1, 1, 1)
        s.update(10)
        self.assertEqual(s.id, 10)
        s = Square(4, 1, 1, 1)
        s.update(10, 7)
        self.assertEqual(s.id, 10)
        self.assertEqual(s.size, 7)
        s = Square(4, 1, 1, 1)
        s.update(10, 7, 7)
        self.assertEqual(s.id, 10)
        self.assertEqual(s.size, 7)
        self.assertEqual(s.x, 7)
        s = Square(4, 1, 1, 1)
        s.update(10, 7, 7, 7)
        self.assertEqual(s.id, 10)
        self.assertEqual(s.size, 7)
        self.assertEqual(s.x, 7)
        self.assertEqual(s.y, 7)
        s = Square(4, 1, 1, 1)
        s.update(**{"id": 66})
        self.assertEqual(s.id, 66)
        s = Square(4, 1, 1, 1)
        s.update(**{"id": 66, "size": 77})
        self.assertEqual(s.id, 66)
        self.assertEqual(s.size, 77)
        s = Square(4, 1, 1, 1)
        s.update(**{"id": 66, "size": 77, "x": 88})
        self.assertEqual(s.id, 66)
        self.assertEqual(s.size, 77)
        self.assertEqual(s.x, 88)
        s = Square(4, 1, 1, 1)
        s.update(**{"id": 66, "size": 77, "x": 88, "y": 99})
        self.assertEqual(s.id, 66)
        self.assertEqual(s.size, 77)
        self.assertEqual(s.x, 88)
        self.assertEqual(s.y, 99)

    def test_create(self):
        """Testing create method"""
        s = Square.create(**{"id": 7})
        self.assertEqual(s.id, 7)
        s = Square.create(**{"id": 7, "size": 8})
        self.assertEqual(s.id, 7)
        self.assertEqual(s.size, 8)
        s = Square.create(**{"id": 7, "size": 8, "x": 9})
        self.assertEqual(s.id, 7)
        self.assertEqual(s.size, 8)
        self.assertEqual(s.x, 9)
        s = Square.create(**{"id": 7, "size": 8, "x": 9, "y": 10})
        self.assertEqual(s.id, 7)
        self.assertEqual(s.size, 8)
        self.assertEqual(s.x, 9)
        self.assertEqual(s.y, 10)

    def test_save_to_file(self):
        """testing save_to_file method"""
        my_list = None
        Square.save_to_file(my_list)
        self.assertTrue(os.path.exists("Square.json"))
        if os.path.exists("Square.json"):
            with open("Square.json", encoding="UTF-8") as ff:
                content = ff.read()
            val = "[]"
            self.assertEqual(content.rstrip(), val)
        os.remove("Square.json")
        my_list = []
        Square.save_to_file(my_list)
        self.assertTrue(os.path.exists("Square.json"))
        if os.path.exists("Square.json"):
            with open("Square.json", encoding="UTF-8") as ff:
                content = ff.read()
            val = "[]"
            self.assertEqual(content.rstrip(), val)
        os.remove("Square.json")
        my_list = [Square(7, 5, 5, 55)]
        Square.save_to_file(my_list)
        self.assertTrue(os.path.exists("Square.json"))
        if os.path.exists("Square.json"):
            with open("Square.json", encoding="UTF-8") as ff:
                content = ff.read()
            val = '[{"id": 55, "size": 7, "x": 5, "y": 5}]'
            self.assertEqual(content.rstrip(), val)
        os.remove("Square.json")

    def test_save_to(self):
        "Edge case for save_to_file"""
        Square._Base__nb_objects = 0
        my_list = [Square(7)]
        Square.save_to_file(my_list)
        self.assertTrue(os.path.exists("Square.json"))
        if os.path.exists("Square.json"):
            with open("Square.json", encoding="UTF-8") as ff:
                content = ff.read()
            val = '[{"id": 1, "size": 7, "x": 0, "y": 0}]'
            self.assertEqual(content.rstrip(), val)

    def test_load_from_file(self):
        """testing load_from_file method"""
        content = Square.load_from_file()
        expected = []
        self.assertEqual(content, expected)
        s = Square(7, 1, 1, 10)
        expected = [s]
        type(s).save_to_file(expected)
        self.assertTrue(os.path.exists("Square.json"))
        content = Square.load_from_file()
        for out, exp in zip(sorted(content), sorted(expected)):
            self.assertEqual(out.to_dictionary(), exp.to_dictionary())
