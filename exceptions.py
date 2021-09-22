a = 2
b = 0

try:
    print(a/b)
except ZeroDivisionError:
    print('Division by zero is not allowed')