import winsound

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
        if self.secondnumber == 0:
            raise ZeroDivisionError("Cannot divide by zero")
        return self.firstnumber / self.secondnumber

class CalculatorApp:
    def get_num(self):
        while True:
            try:
                first_number = float(input("Enter first number: "))
                second_number = float(input("Enter second number: "))
                return first_number, second_number
            except ValueError:
                print("Only numbers are accepted")

    def operations(self):
        print("\nChoose operation:")
        print("+ Addition")
        print("- Subtraction")
        print("* Multiplication")
        print("/ Division")

        while True:
            operation = input("Enter operation (+, -, *, /): ")
            if operation in ["+", "-", "*", "/"]:
                return operation
            print("Invalid operation")

    def calculator(self, operation, first_number, second_number):
        if operation == "+":
            return Addition(first_number, second_number)
        elif operation == "-":
            return Subtraction(first_number, second_number)
        elif operation == "*":
            return Multiplication(first_number, second_number)
        else:
            return Division(first_number, second_number)

    def sound_effect(self):
        try:
            winsound.PlaySound("tada.wav", winsound.SND_FILENAME)
        except:
            pass

    def continue_calculator(self):
        while True:
            user_choice = input("\nWould you like to continue? (y/n): ").lower()
            if user_choice in ['y', 'n']:
                return user_choice == "y"
            print("Invalid choice")

    def run(self):
        print("Simple App Calculator")

        while True:
            operation = self.operations()
            first_number, second_number = self.get_num()

            try:
                calculator  = self.calculator(operation, first_number, second_number)
                result = calculator.calculate()
                print("Result:", result)

                self.sound_effect()

            except ZeroDivisionError as error:
                print("Error", error)

            if not self.continue_calculator():
                print("Thanks for using this calculator")
                break

CalculatorApp().run()