
# Classes and objects
class Stock:
    def __init__(self, ticker, price):
        self.ticker = ticker
        self.price = price
    def display(self):
        print(f"Stock: {self.ticker}, Price: ${self.price}")
apple = Stock("AAPL", 150)
apple.display()

# Modules and packages (Assuming a module 'example_module' exists)
# from example_module import example_function
# example_function()

# Exceptions
try:
    result = 10 / 0
except ZeroDivisionError:
    print("Cannot divide by zero!")
