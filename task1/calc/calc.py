def calculator(num1, num2, operator):
    if operator == '+':
        return num1 + num2
    elif operator == '-':
        return num1 - num2
    elif operator == '*':
        return num1 * num2
    elif operator == '/':
        return num1 / num2
    elif num1 == 0 and num2 == 0 and operator == '0':
        return 'exit'
    else:
        return '잘못 입력하셨습니다'
