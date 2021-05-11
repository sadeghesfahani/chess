class Calculator:
    final = 0
    last_operator = ""
    def __init__(self):
        self.x = float()
        self.y = float()
        self.operator = str()
        self.operators = "+-/*"

    def calculate(self):

        self.x = Calculator.final

        try:
            self.x = float(input("Enter first number: "))
        except ValueError:
            raise NumberError(1, "it's not a number")
        except TypeError:
            raise NumberError(1, "it's not a number")
        try:
            self.y = float(input("Enter second number: "))
        except ValueError:
            raise NumberError(2, "it's not a number")
        except TypeError:
            raise NumberError(2, "it's not a number")
        self.operator = input("please input operator (*/+-): ")
        if len(self.operator) != 1 or self.operator not in self.operators:
            raise OperatorError(self.operator, "Operator is not valid")
        result = eval(f"{self.x}{self.operator}{self.y}")
        self.x = result
        self.y = 0
        Calculator.last_operator=self.operator
        self.operator = ""
        return result


class NumberError(Exception):
    def __init__(self, arg, message):
        self.message = message
        self.argss=arg


class OperatorError(Exception):
    def __init__(self, arg, message):
        self.message = message
        self.argss = arg

calc=Calculator()


try:
    print(calc.calculate())
except NumberError as obj:
    print(f"{obj.argss} Parameter Error: {obj.message}")
except OperatorError as opt:
    print(f"{opt.argss} {opt.message}")
except ZeroDivisionError:
    print("second number must be zero excluded")
