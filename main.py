#import matplotlib.pyplot as plt
#import numpy as np

d = 0
num = 0
digitCount = [0, 0, 0, 0, 0, 0, 0, 0, 0]
y = 0  # variable for checking leading digit of c when c > 10
c = int(input("Enter a number: "))  # variable to iterate through collatz conjecture
print("We're going to check for the Collatz Conjecture or 3n+1 problem")
print("This might be a very bad idea")
print("Your starting number: " + str(c))
print("Time to see the hailstone numbers: ")
while d != 1:
    if c % 2 == 0:
        c = int(c / 2)  # even number divided by 2. The operation is within int() as python 3.x returns a float...
        print(c)        # ... after division even if both inputs are integers
        num = num + 1
        if c > 10:
            y = c
            while y > 10:  # if c>10, y/10 eventually gives leading digit
                y = int(y / 10)
            digitCount[y - 1] = digitCount[y - 1] + 1
            d = c  # if c = 1 after operations, then loop should end
        elif c < 10:
            digitCount[c - 1] = digitCount[c - 1] + 1
            d = c
    elif c % 2 != 0:
        c = int((3 * c) + 1)
        print(c)
        num = num + 1
        if c > 10:
            y = c
            while y >= 10:  # if c>10, y/10 eventually gives leading digit
                y = int(y / 10)
            digitCount[y - 1] = digitCount[y - 1] + 1
            d = c
        elif c < 10:
            digitCount[c - 1] = digitCount[c - 1] + 1
            d = c
print("Number of hailstone numbers is: " + str(num))
