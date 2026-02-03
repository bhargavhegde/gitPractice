import math

class Calculator:
        def __init__(self):
            print("Calculator initialized")

        def multiply(self, a, b):
            return a * b

        def divide(self, a, b):
            return a / b
        
        def add(self, a, b):
            return a + b
        
        def subtract(self, a, b):
            return a - b
        
        def power(self, a, b):
            return a**b

        def sqrt(self, a):
            return math.sqrt(a)

obj=Calculator()

print(obj.add(10, 20))
print(obj.subtract(10, 20))
print(obj.multiply(10, 20))
print(obj.divide(10, 20))
print(obj.power(10, 20))
print(obj.sqrt(100))