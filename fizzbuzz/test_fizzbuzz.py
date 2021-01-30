from unittest import TestCase
from fizzbuzz import fizzbuzz


class TestFizzBuzz(TestCase):
    def test_always_true(self):
        self.assertEqual(True, True)

    def test_should_return_1_when_input_is_1(self):
        self.assertEqual(fizzbuzz(1), 1)

    def test_should_return_2_when_input_is_2(self):
        self.assertEqual(fizzbuzz(2), 2)

    def test_should_return_3_when_input_is_3(self):
        self.assertEqual(fizzbuzz(3), "fizz")

    def test_should_return_4_when_input_is_4(self):
        self.assertEqual(fizzbuzz(4), 4)

    def test_should_return_5_when_input_is_buzz(self):
        self.assertEqual(fizzbuzz(5), "buzz")

    def test_should_return_6_when_input_is_fizz(self):
        self.assertEqual(fizzbuzz(6), "fizz")

    def test_should_return_7_when_input_is_7(self):
        self.assertEqual(fizzbuzz(7), 7)

    def test_should_return_8_when_input_is_8(self):
        self.assertEqual(fizzbuzz(8), 8)

    def test_should_return_9_when_input_is_9(self):
        self.assertEqual(fizzbuzz(9), "fizz")

    def test_should_return_10_when_input_is_10(self):
        self.assertEqual(fizzbuzz(10), "buzz")
