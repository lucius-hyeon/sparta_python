# class Calcurator():
#     def calculator(self, num1, num2, operator):
#         if operator == '+':
#             return num1 + num2
#         elif operator == '-':
#             return num1 - num2
#         elif operator == '*':
#             return num1 * num2
#         elif operator == '/':
#             return num1 / num2
#         elif num1 == 0 and num2 == 0 and operator == '0':
#             return 'exit'

#     def main(self):
#         num1, operator, num2 = input().split()

#         try:
#             result = self.calculator(int(num1), int(num2), operator)
#             print(result)
#         except ZeroDivisionError:
#             print('0으로 나눌 수 없습니다')
#         except ValueError:
#             print('숫자만 입력 가능합니다')


# calc = Calcurator()
# calc.main()


class Calc():
    is_value = False

    def set_number(self, x, y):
        try:
            self.x = int(x)
            self.y = int(y)
            print('numbers', x, y)
            self.is_value = True
        except ValueError:
            print('숫자를 입력 하세요')

    def puls(self):
        if self.is_value == True:
            return self.x + self.y

    def minus(self):
        if self.is_value == True:
            return self.x - self.y

    def mulitple(self):
        if self.is_value == True:
            return self.x * self.y

    def divide(self):
        try:
            if self.is_value == True:
                return self.x / self.y
        except ZeroDivisionError:
            print('0으로 나눌 수 없습니다')


calc = Calc()
calc.set_number('2', '4')
print(calc.puls())
print(calc.minus())
print(calc.mulitple())
print(calc.divide())
