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
        return self.firstnumber / self.secondnumber