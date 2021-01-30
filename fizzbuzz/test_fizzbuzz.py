from unittest import TestCase
from fizzbuzz import fizzbuzz


class TestFizzBuzz(TestCase):
    def test_always_true(self):
        self.assertEqual(True, True)

    def test_should_return_number_when_inputs_are_not_multiplied_by_3_and_5(self):
        for number in [1, 2, 4, 7, 8, 11, 13, 14, 16, 17, 19]:
            self.assertEqual(fizzbuzz(number), number)

    def test_should_return_fizz_when_inputs_are_multiplied_by_3(self):
        for number in [3, 6, 9, 12, 18]:
            self.assertEqual(fizzbuzz(number), "fizz")

    def test_should_return_buzz_when_inputs_are_multiplied_by_5(self):
        for number in [5, 10, 20]:
            self.assertEqual(fizzbuzz(number), "buzz")

    def test_should_return_buzz_when_inputs_are_multiplied_by_3_and_5(self):
        for number in [15, 30]:
            self.assertEqual(fizzbuzz(number), "fizzbuzz")
