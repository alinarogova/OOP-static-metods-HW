from math import gcd
# Завдання 1
# До вже реалізованого класу «Дроб» додайте статичний метод, який при
# виклику повертає кількість створених об'єктів класу «Дроб».
print("Task 1".center(60, "="))


class Fraction:
    cnt = 0

    def __init__(self, num, denom):
        Fraction.cnt += 1
        self.num = num/gcd(int(num), int(denom))
        self.denom = denom/gcd(int(num), int(denom))
        if self.denom < 0:
            self.num *= -1
            self.denom *= -1
        elif self.denom == 0:
            raise ZeroDivisionError

    def __str__(self):
        # print("Fraction.cnt", Fraction.cnt , end=' ')
        # Fraction.cnt -= 1
        return f"{int(self.num)}/{int(self.denom)}"

    def __add__(self, other):
        # Fraction.cnt -= 1
        n = self.num*other.denom + other.num*self.denom
        d = self.denom*other.denom
        # print(n, d)
        return Fraction(n, d)

    def __sub__(self, other):
        n = self.num*other.denom - other.num*self.denom
        d = self.denom*other.denom
        # print(n, d)
        return Fraction(n, d)

    def __truediv__(self, other):  # __div__(self, other):
        n = self.num*other.denom
        d = self.denom*other.num
        return Fraction(n, d)

    def __mul__(self, other):
        n = self.num*other.num
        d = self.denom*other.denom
        return Fraction(n, d)

    @staticmethod
    def count_fraction():
        return Fraction.cnt


f1 = Fraction(8, -10)
f2 = Fraction(3, 24)
print(f1)
print(f2)
print("Sum", f1+f2)
print("Dif", f1-f2)
print("Mult", f1*f2)
print("Div", f1/f2)
print(Fraction.count_fraction())
print("Div", f1/f2)
print(Fraction.count_fraction())
# Завдання 2
# Створіть клас для конвертування температури з Цельсія у Фаренгейт і навпаки.
# У класу має бути два статичні методи: для перекладу з Цельсія до Фаренгейта і для перекладу з Фаренгейта до Цельсія.
# Також клас повинен вважати кількість підрахунків температури та повертати це значення з допомогою статичного методу.
print("Task 2".center(60, "="))


class ConvertingTemperature:
    @staticmethod
    def CtoF(temperature):
        return temperature*9/5+32

    @staticmethod
    def FtoC(temperature):
        return (temperature-32)*5/9


print(ConvertingTemperature.CtoF(32))
print(ConvertingTemperature.FtoC(89.6))
# Завдання 3
# Створіть клас для перекладу з метричної системи в англійську та навпаки.
# Функціональність необхідна реалізувати як статичних методів. Обов'язково реалізуйте переведення заходів довжини
# 1 дюйм (inch) = 12 ліній = 72 пункти = 1000 мілів = 2,54 см
# 1 ярд (yard) = 3 фути = 0,9144 м
# 1 статутна миля (statute mile) = 8 фурлонгів = 5280 футів = 1609,344 м
print("Task 3".center(60, "="))


class Converting:
    @staticmethod
    def inch_to_sm(lenght):
        return lenght * 2.54

    @staticmethod
    def sm_to_inch(lenght):
        return lenght / 2.54

    @staticmethod
    def yard_to_m(lenght):
        return lenght * 0.9144

    @staticmethod
    def m_to_yard(lenght):
        return lenght / 0.9144

    @staticmethod
    def mile_to_m(lenght):
        return lenght * 1609.344

    @staticmethod
    def m_to_mile(lenght):
        return lenght / 1609.344


print("1 inch = ", Converting.inch_to_sm(1), "sm", sep="")
print("1 sm = ", Converting.sm_to_inch(1), "inch", sep="")
print("1 mile = ", Converting.mile_to_m(1), "m", sep="")
print("1 m = ", Converting.m_to_mile(1), "mile", sep="")
print("1 yard = ", Converting.yard_to_m(1), "m", sep="")
print("1 m = ", Converting.m_to_yard(1), "yard", sep="")
