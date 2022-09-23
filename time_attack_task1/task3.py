def get_even_numbers(numbers):
    result = []
    for number in numbers:
        if number % 2 == 0:
            result.append(number)
    return result


def get_some_numbers(numbers):
    result = []
    for number in numbers:
        if number % 3 == 0 and number % 15 != 0:
            result.append(number*10)
    return result


def main():
    numbers = []  # 1 ~ 10000
    for i in range(1, 10001):
        numbers.append(i)
    even_numbers = get_even_numbers(numbers)
    some_numbers = get_some_numbers(numbers)
    print(even_numbers)  # [2, 4, 6, ...]
    print(some_numbers)  # [30, 60, 90, 120, 180, ...]


main()
