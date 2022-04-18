import matplotlib.pyplot as plt
import numpy as np

d = 0  # this is the stop condition variable for while loop to be used as a do-while loop
num = 0  # number of hailstone numbers
digitCount = np.array([0, 0, 0, 0, 0, 0, 0, 0, 0])
hailstoneNums = np.array([0])  # Putting starting element as 0 so index of hailstone numbers matches their position
hailstoneNumsCount = np.array([0])  # count of hailstone nums for plotting
y = 0  # variable for checking leading digit of c when c > 10
c = int(input("Enter a number: "))  # variable to iterate through collatz conjecture, needs to be int
print("We're going to check for the Collatz Conjecture or 3n+1 problem")
print("This might be a very bad idea")
print("Your starting number: " + str(c))
print("Time to see the hailstone numbers: ")
while d != 1:  # d is used because in c = 1 case, this will not run and python does not have do-while
    if c % 2 == 0:
        c = int(c / 2)  # even number divided by 2. The operation is within int() as python 3.x returns a float...
        print(c)  # ... after division even if both inputs are integers
        hailstoneNums = np.append(hailstoneNums, c)  # adds hailstone number to the array
        num = num + 1
        hailstoneNumsCount = np.append(hailstoneNumsCount, num)
        if c >= 10:
            y = c
            while y >= 10:  # if c>10, y/10 eventually gives leading digit
                y = int(y / 10)
            digitCount[y - 1] = digitCount[y - 1] + 1
            d = c  # if c = 1 after operations, then loop should end
        elif c < 10:
            digitCount[c - 1] = digitCount[c - 1] + 1
            d = c
    elif c % 2 != 0:
        c = int((3 * c) + 1)
        print(c)
        hailstoneNums = np.append(hailstoneNums, c)
        num = num + 1
        hailstoneNumsCount = np.append(hailstoneNumsCount, num)
        if c >= 10:
            y = c
            while y >= 10:  # if c>10, y/10 eventually gives leading digit
                y = int(y / 10)
            digitCount[y - 1] = digitCount[y - 1] + 1
            d = c
        elif c < 10:
            digitCount[c - 1] = digitCount[c - 1] + 1
            d = c
print("Number of hailstone numbers is: " + str(num))
hold = np.amax(digitCount)  # Highest occurring leading digit
ghn = np.amax(hailstoneNums)  # Greatest hailstone number
print("Greatest Hailstone Number is: " + str(ghn))
xpoints = hailstoneNumsCount  # x-axis for plot of hailstone numbers, last digit is the number of hailstone nums
ypoints = hailstoneNums  # y-axis for plot of hailstone numbers, last digit is the greatest hailstone number
plt.plot(xpoints, ypoints)
plt.show()
bars = ('1', '2', '3', '4', '5', '6', '7', '8', '9')
plt.bar(bars, digitCount, color='g')
plt.show()

