from typing import List
from unittest import TestCase, main
from fizzbuzz import (
    BuzzRule,
    FizzBuzzRule,
    FizzRule,
    FizzBuzz,
    Rule,
)


class TestFizzBuzz(TestCase):
    def setUp(self):
        rules: List[Rule] = [
            FizzBuzzRule(),
            BuzzRule(),
            FizzRule(),
        ]
        self.fizzbuzz = FizzBuzz(rules)

    def test_should_return_number_when_inputs_are_not_multiplied_by_3_and_5(self):
        for number in [1, 2, 4, 7, 8, 11, 13, 14, 16, 17, 19]:
            self.assertEqual(self.fizzbuzz.say(number), str(number))

    def test_should_return_fizz_when_inputs_are_multiplied_by_3(self):
        for number in [3, 6, 9, 12, 18]:
            self.assertEqual(self.fizzbuzz.say(number), "fizz")

    def test_should_return_buzz_when_inputs_are_multiplied_by_5(self):
        for number in [5, 10, 20]:
            self.assertEqual(self.fizzbuzz.say(number), "buzz")

    def test_should_return_buzz_when_inputs_are_multiplied_by_3_and_5(self):
        for number in [15, 30]:
            self.assertEqual(self.fizzbuzz.say(number), "fizzbuzz")


if __name__ == "__main__":
    main()