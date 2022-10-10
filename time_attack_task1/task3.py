def get_even_numbers(numbers):
    # case 1
    """
    result = [x for x in numbers if x % 2 == 0]
    """
    # case 2
    """
    result = list(filter(lambda x: x % 2 == 0, numbers))
    """

    result = []
    for number in numbers:
        if number % 2 == 0:
            result.append(number)

    return result


def get_some_numbers(numbers):
    # case 1
    """
    result = list(filter(lambda x: x % 3 == 0 and x % 15 != 0, numbers))
    result = list(map(lambda x: x*10, result))
    """
    # case 2
    result = [x*10 for x in numbers if x % 3 == 0 and x % 15 != 0]

    # result = []
    # for number in numbers:
    #     if number % 3 == 0 and number % 15 != 0:
    #         result.append(number*10)
    return result


def main():
    # case 1
    """
    numbers = list(range(1, 10001))
    """
    # case 2
    """
    numbers = [x for x in range(1, 10001)]
    """
    numbers = []  # 1 ~ 10000
    for i in range(1, 10001):
        numbers.append(i)

    even_numbers = get_even_numbers(numbers)
    some_numbers = get_some_numbers(numbers)
    print(even_numbers)  # [2, 4, 6, ...]
    print(some_numbers)  # [30, 60, 90, 120, 180, ...]


main()
