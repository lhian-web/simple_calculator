class Calculator:
    def __init__(self, firstnumber, secondnumber):
        self.firstnumber = firstnumber
        self.secondnumber = secondnumber

    def calculate(self):
        pass

class Addition(Calculator):
    def calculate(self):
        return self.firstnumber + self.secondnumber

class Subtraction(Calculator):
    def calculate(self):
        return self.firstnumber - self.secondnumber

class Multiplication(Calculator):
    def calculate(self):
        return self.firstnumber * self.secondnumber

class Division(Calculator):
    def calculate(self):
        if self.firstnumber != 0:
            raise ZeroDivisionError("Cannot divide by zero")
        return self.firstnumber / self.secondnumber

def get_num(self):
    while True:
        try:
            first_number = float(input("Enter first number: "))
            second_number = float(input("Enter second number: "))
            return first_number, second_number
        except ValueError:
            print("Only numbers are accepted")
