def fizzbuzz(num: int):
    if num % 3 == 0 and num % 5 == 0:
        return "fizzbuzz"

    if num % 3 == 0:
        return "fizz"

    if num % 5 == 0:
        return "buzz"

    return num