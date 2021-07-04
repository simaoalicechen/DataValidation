"""
Testing the IntegerField without BaseValidator
"""


import unittest

from app1.IntegerField import IntegerField


class TestIntegerField(unittest.TestCase):
    @staticmethod
    def create_test_class(min_, max_):
        obj = type('TestClass', (), {'age': IntegerField(min_, max_)})
        return obj()

    def test_set_age_ok(self):
        """Tests that valid values can be assigned/retrieved"""
        min_ = 5
        max_ = 10
        obj = self.create_test_class(min_, max_)
        valid_values = range(min_, max_)

        for i, value in enumerate(valid_values):
            with self.subTest(test_number=i):
                obj.age = value
                self.assertEqual(value, obj.age)

    def test_set_age_invalid(self):
        """Tests that invalid values raise ValueErrors"""
        min_ = -10
        max_ = 10
        obj = self.create_test_class(min_, max_)
        bad_values = list(range(min_ - 5, min_))
        bad_values += list(range(max_ + 1, max_ + 5))
        bad_values += [10.5, 1 + 0j, 'abc', (1, 2)]

        for i, value in enumerate(bad_values):
            with self.subTest(test_number=i):
                with self.assertRaises(ValueError):
                    obj.age = value

    def test_class_get(self):
        """Tests that class attribute retrieval returns the descriptor instance"""
        obj = self.create_test_class(0, 0)
        obj_class = type(obj)
        self.assertIsInstance(obj_class.age, IntegerField)

    def test_set_age_min_only(self):
        """Tests that we can specify a min value only"""
        min_ = 0
        max_ = None
        obj = self.create_test_class(min_, max_)
        values = range(min_, min_ + 100, 10)
        for i, value in enumerate(values):
            with self.subTest(test_number=i):
                obj.age = value
                self.assertEqual(value, obj.age)

    def test_set_age_max_only(self):
        """Tests that we can specify a max value only"""
        min_ = None
        max_ = 10
        obj = self.create_test_class(min_, max_)
        values = range(max_ - 100, max_, 10)
        for i, value in enumerate(values):
            with self.subTest(test_number=i):
                obj.age = value
                self.assertEqual(value, obj.age)

    def test_set_age_no_limits(self):
        """Tests that we can use IntegerField without any limits at all"""
        min_ = None
        max_ = None
        obj = self.create_test_class(min_, max_)
        values = range(-100, 100, 10)
        for i, value in enumerate(values):
            with self.subTest(test_number=i):
                obj.age = value
                self.assertEqual(value, obj.age)

#   run_tests(TestIntegerField)

