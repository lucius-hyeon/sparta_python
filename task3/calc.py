class Calc():
    def set_number(self, num1, num2):
        self.num1 = num1
        self.num2 = num2

    def puls(self):
        return self.num1 + self.num2

    def minus(self):
        return self.num1 - self.num2

    def multiple(self):
        return self.num1 * self.num2

    def divide(self):
        return self.num1 / self.num2


calc = Calc()
calc.set_number(20, 10)
print(calc.puls())
print(calc.minus())
print(calc.multiple())
print(calc.divide())
