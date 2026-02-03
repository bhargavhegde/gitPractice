class Calculator:
        def __init__(self):
            print("Calculator initialized")

        def multiply(self, a, b):
            return a * b

        def divide(self, a, b):
            return a / b

obj=Calculator()
print(obj.multiply(10, 20))