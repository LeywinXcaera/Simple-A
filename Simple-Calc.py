# Simple Calculator
a = int(input("Enter the first number: "))
b = int(input("Enter the second number: "))

print("1 = add,2 = subtract,3 = divide,4 = multiply")
c = int(input(" :"))

if c == 1:
    d = a + b
    print(d)
elif c == 2:
    d = a - b
    print(d)
elif c == 3:
    d = a / b
    print(d)
else:
    d = a * b
    print(d)
