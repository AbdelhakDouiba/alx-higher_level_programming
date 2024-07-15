#!/usr/bin/python3
"""
Testing "base" Module
"""


import unittest
from models.base import Base


class TestBaseClass(unittest.TestCase):
    """Testing Base class"""

    def setUp(self):
        """Set each method"""
        Base._Base__nb_objects = 0

    def test_no_id(self):
        """testing with no id"""
        dummy = Base()
        self.assertEqual(dummy.id, 1)

    def test_no_id_two_times(self):
        """testing for id with calling base two times"""
        dummy = Base()
        Pdummy = Base()
        self.assertEqual(Pdummy.id, 2)

    def test_mixed_ids(self):
        """tesing mixed ids"""
        d1 = Base()
        d2 = Base()
        d3 = Base(17)
        d4 = Base()
        self.assertEqual(d1.id, 1)
        self.assertEqual(d2.id, 2)
        self.assertEqual(d3.id, 17)
        self.assertEqual(d4.id, 3)

    def test_id_as_input(self):
        """testing with a valid id as an input"""
        dummy = Base(47)
        self.assertEqual(dummy.id, 47)

    def test_more_args(self):
        """testing for exceeding the args number"""
        with self.assertRaises(TypeError):
            mm = Base(11, 12)
        with self.assertRaises(TypeError):
            mm = Base(7, "Thirty")

    def test_access_private(self):
        """testing accessing private attribute"""
        mm = Base()
        with self.assertRaises(AttributeError):
            tmp = mm.__Base__nb_objects

    def test_to_json_string(self):
        """testing to_json_sting method"""
        dummy = Base(47)
        string = dummy.to_json_string(None)
        self.assertEqual(string, "[]")
        string = dummy.to_json_string([])
        self.assertEqual(string, "[]")
