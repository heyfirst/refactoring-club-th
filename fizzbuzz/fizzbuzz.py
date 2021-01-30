from abc import abstractmethod
from typing import List


class Rule:
    @abstractmethod
    def handle(self, num: int) -> bool:
        pass

    @abstractmethod
    def say(self) -> str:
        pass


class FizzBuzzRule(Rule):
    def handle(self, num: int) -> bool:
        return num % 15 == 0

    def say(self) -> str:
        return "fizzbuzz"


class FizzRule(Rule):
    def handle(self, num: int) -> bool:
        return num % 3 == 0

    def say(self) -> str:
        return "fizz"


class BuzzRule(Rule):
    def handle(self, num: int) -> bool:
        return num % 5 == 0

    def say(self) -> str:
        return "buzz"


class FizzBuzz:
    rules: List[Rule] = []

    def __init__(self, rules: List[Rule]):
        self.rules = rules

    def say(self, num: int) -> str:
        for rule in self.rules:
            if rule.handle(num):
                return rule.say()

        return str(num)
