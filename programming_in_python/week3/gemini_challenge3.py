class Addingmachine:
    def __init__(self):
        self.num1 = 0
        self.num2 = 0
        
    def add(self, a, b):
        return a + b
num = Addingmachine()
print('sum = ',num.add(5, 6))