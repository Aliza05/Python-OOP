#in Git repository: Python-OOP


class Calculator:
    def __init__(self, digit1, digit2):
        self.digit1 = digit1
        self.digit2 = digit2

    def add(self):
        print(f"The sum of digits: {self.digit1 + self.digit2}")

    def subtract(self):
        print(f"The subtraction of digits: {self.digit1 - self.digit2}")

    def multiply(self):
        print(f"The multiplication of digits: {self.digit1 * self.digit2}")

    def divide(self):
        print(f"The multiplication of digits: {self.digit1 / self.digit2}")


digit_1 = float(input("Enter first digit: "))
digit_2 = float(input("Enter second digit: "))
calculate = Calculator(digit_1, digit_2)
calculate.add()
calculate.subtract()
calculate.multiply()
calculate.divide()
