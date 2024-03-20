class Calculator:
    def __init__(self):
        self.number1 = 0
        self.number2 = 0

    def add(self, a, b):
        return a + b

    def subtract(self, a, b):
        return a - b

    def multiply(self, a, b):
        return a * b

    def divide(self, a, b):
        if b != 0:
            return a / b
        else:
            raise ValueError("Cannot divide by zero")
        
value = Calculator()
print(value.add(5, 6))
print(value.subtract(9, 6))
print(value.multiply(5, 6))
print(value.divide(9, 3))

