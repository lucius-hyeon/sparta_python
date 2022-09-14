class Area():
    def __init__(self, num1, num2):
        self.num1 = num1
        self.num2 = num2

    def square(self):
        return self.num1 * self.num2

    def triangle(self):
        return self.num1 * self.num2 / 2

    def circle(self):
        return (self.num1 / 2) ** 2


area = Area(10, 20)
print(area.square())
print(area.triangle())
print(area.circle())
