"""
Testing the CharField without BaseValidator
"""

import unittest

from app1.CharField import CharField


class TestCharField(unittest.TestCase):
    @staticmethod
    def create_test_class(min_, max_):
        obj = type('TestClass', (), {'name': CharField(min_, max_)})
        return obj()

    def test_set_name_ok(self):
        """Tests that valid values can be assigned/retrieved"""
        min_ = 1
        max_ = 10
        obj = self.create_test_class(min_, max_)
        valid_lengths = range(min_, max_)

        for i, length in enumerate(valid_lengths):
            value = 'a' * length
            with self.subTest(test_number=i):
                obj.name = value
                self.assertEqual(value, obj.name)

    def test_set_name_invalid(self):
        """Tests that invalid values raise ValueErrors"""
        min_ = 5
        max_ = 10
        obj = self.create_test_class(min_, max_)
        bad_lengths = list(range(min_ - 5, min_))
        bad_lengths += list(range(max_ + 1, max_ + 5))
        for i, length in enumerate(bad_lengths):
            value = 'a' * length
            with self.subTest(test_number=i):
                with self.assertRaises(ValueError):
                    obj.name = value

    def test_class_get(self):
        """Tests that class attribute retrieval returns the descriptor instance"""
        obj = self.create_test_class(0, 0)
        obj_class = type(obj)
        self.assertIsInstance(obj_class.name, CharField)

    def test_set_name_min_only(self):
        """Tests that we can specify a min length only"""
        min_ = 0
        max_ = None
        obj = self.create_test_class(min_, max_)
        valid_lengths = range(min_, min_ + 100, 10)
        for i, length in enumerate(valid_lengths):
            value = 'a' * length
            with self.subTest(test_number=i):
                obj.name = value
                self.assertEqual(value, obj.name)

    def test_set_name_min_negative_or_none(self):
        """Tests that setting a negative or None length results in a zero length"""
        obj = self.create_test_class(-10, 100)
        self.assertEqual(type(obj).name._min, 0)
        self.assertEqual(type(obj).name._max, 100)

        obj = self.create_test_class(None, None)
        self.assertEqual(type(obj).name._min, 0)
        self.assertIsNone(type(obj).name._max)

    def test_set_name_max_only(self):
        """Tests that we can specify a max length only"""
        min_ = None
        max_ = 10
        obj = self.create_test_class(min_, max_)
        valid_lengths = range(max_ - 100, max_, 10)
        for i, length in enumerate(valid_lengths):
            value = 'a' * length
            with self.subTest(test_number=i):
                obj.name = value
                self.assertEqual(value, obj.name)

    def test_set_name_no_limits(self):
        """Tests that we can use CharField without any limits at all"""
        min_ = None
        max_ = None
        obj = self.create_test_class(min_, max_)
        valid_lengths = range(0, 100, 10)
        for i, length in enumerate(valid_lengths):
            value = 'a' * length
            with self.subTest(test_number=i):
                obj.name = value
                self.assertEqual(value, obj.name)


def run_tests(test_class):
    suite = unittest.TestLoader().loadTestsFromTestCase(test_class)
    runner = unittest.TextTestRunner(verbosity=2)
    result = runner.run(suite)

#    run_tests(TestCharField)

