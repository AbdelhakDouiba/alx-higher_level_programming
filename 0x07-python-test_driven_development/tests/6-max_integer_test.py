#!/usr/bin/python3
"""Unittest for max_integer([..])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer

class TestMaxInteger(unittest.TestCase):
    '''Testing the "max_integer" module'''
    def test_documentation(self):
        '''Testing the documenatation'''
        Mdoc = __import__('6-max_integer').__doc__
        self.assertTrue(len(Mdoc) > 0)
        Mdoc = __import__('6-max_integer').max_integer.__doc__
        self.assertTrue(len(Mdoc) > 0)

    def test_normal_cases(self):
        '''Testing normal cases'''
        self.assertEqual(max_integer([1, 2, 3, 4]), 4)
        self.assertEqual(max_integer([1, 3, 4, 2]), 4)
        self.assertEqual(max_integer([1, 3, 4.9, 2]), 4.9)
        self.assertEqual(max_integer(["olala", "sunny"]), "sunny")
        self.assertEqual(max_integer("hello"), "o")

    def test_single_value(self):
        '''Testing single value'''
        self.assertEqual(max_integer([0]), 0)
        self.assertEqual(max_integer([10]), 10)

    def test_non_list(self):
        '''Testing non list as a value'''
        self.assertRaises(TypeError, max_integer, 5)
        self.assertRaises(TypeError, max_integer, float('inf'))

    def test_None_input(self):
        '''Testing None as input'''
        self.assertRaises(TypeError, max_integer, None)

    def test_empty_input(self):
        '''Testing using empty input'''
        self.assertIsNone(max_integer([]))
        self.assertIsNone(max_integer())

    def test_more_args(self):
        '''Testing using more than one argument'''
        self.assertRaises(TypeError, max_integer, [1, 2, 3, 4], [1, 2])
        self.assertRaises(TypeError, max_integer, [1], [1, 2])

    def test_non_int_element(self):
        '''Testing using non int elements'''
        self.assertRaises(TypeError, max_integer, [1, 2, "hello", 4])

if __name__ == '__main__':
    unittest.main()
