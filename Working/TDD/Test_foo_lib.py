import unittest
import foo_lib


class Test_foo_lib(unittest.TestCase):

    def test_foo1_general1(self):
        self.assertEqual(3, foo_lib.foo1(9))  # expected value, actual value

    def test_foo1_general2(self):
        self.assertEqual(4, foo_lib.foo1(16))

    def test_foo1_unusual_negative(self):
        self.assertRaises(ValueError, foo_lib.foo1, -16)

    def test_foo1_unusual_negative_specific_msg(self):
        with self.assertRaises(ValueError) as err:  # 'err' stores info about the error that is generated from code
            foo_lib.foo1(-16)

        self.assertEqual("Cannot square root a negative number", str(err.exception))  # test for equivalent of the error
        # the message is what we expect from the error we test to see if that value comes up when there is an error

    def test_fooList1_general(self):
        self.assertEqual(6, foo_lib.fooList([1, 2, 3]))

    def test_fooList1_corner_singleValue(self):
        self.assertEqual(5, foo_lib.fooList([5]))

    def test_fooList1_unusual_emptyList(self):
        self.assertRaises(ValueError, foo_lib.fooList([]))

    def test_fooList1_unusual_emptyList_specific_msg(self):
        with self.assertRaises(ValueError) as err:
            foo_lib.fooList([])

        self.assertEqual("Cannot process empty list", str(err.exception))
